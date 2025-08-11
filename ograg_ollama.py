import json
import numpy as np
from typing import List, Dict, Set, Tuple, Any, Optional
from dataclasses import dataclass
from collections import defaultdict
import ollama
from sentence_transformers import SentenceTransformer
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import logging
import pickle
from pathlib import Path
from rdflib import Graph

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Hypernode:
    """Represents a hypernode in the hypergraph"""
    key: str  # Concatenated subject + attribute
    value: str
    embedding: np.ndarray = None

@dataclass
class Hyperedge:
    """Represents a hyperedge (fact) in the hypergraph"""
    nodes: Set[str]  # Set of hypernode keys
    fact_text: str

class OllamaClient:
    """Wrapper for Ollama API"""
    def __init__(self, model_name: str = "llama3.1:8b"):
        self.model_name = model_name
        
    def generate(self, prompt: str, temperature: float = 0.1) -> str:
        """Generate text using Ollama"""
        try:
            response = ollama.generate(
                model=self.model_name, 
                prompt=prompt,
                options={"temperature": temperature}
            )
            return response['response']
        except Exception as e:
            logger.error(f"Ollama generation error: {e}")
            return ""

class OGRAG:
    """Ontology-Grounded Retrieval Augmented Generation"""
    
    def __init__(self, 
                 llm_model: str = "llama3.1:8b",
                 embedding_model: str = "all-MiniLM-L6-v2"):
        self.llm = OllamaClient(llm_model)
        self.embedder = SentenceTransformer(embedding_model)
        self.hypergraph = nx.Graph()
        self.hypernodes = {}
        self.hyperedges = []
        self.ontology = {}
        
    def load_ontology(self, ontology_path: str):
        """Load ontology from file (supports TTL/RDF and JSON-LD formats)"""
        from rdflib import Graph
        
        file_ext = Path(ontology_path).suffix.lower()
        
        if file_ext in ['.ttl', '.rdf', '.owl', '.n3', '.nt']:
            # Load RDF/TTL file and convert to JSON-LD
            logger.info(f"Loading {file_ext} ontology and converting to JSON-LD...")
            g = Graph()
            
            # Determine format based on extension
            format_map = {
                '.ttl': 'turtle',
                '.rdf': 'xml',
                '.owl': 'xml',
                '.n3': 'n3',
                '.nt': 'nt'
            }
            rdf_format = format_map.get(file_ext, 'turtle')
            
            try:
                g.parse(ontology_path, format=rdf_format)
                
                # Convert to JSON-LD
                jsonld_str = g.serialize(format='json-ld', indent=2)
                json_data = json.loads(jsonld_str)

                # If the result is a list, wrap it in a dict under @graph
                if isinstance(json_data, list):
                    self.ontology = {'@graph': json_data}
                else:
                    self.ontology = json_data
                                
                # Extract context from the ontology if available
                if '@context' in self.ontology:
                    logger.info("Found @context in ontology")
                else:
                    # Generate basic context from namespaces
                    context = {}
                    for prefix, namespace in g.namespaces():
                        if prefix:  # Skip default namespace
                            context[prefix] = str(namespace)
                    if context:
                        self.ontology['@context'] = context
                        logger.info(f"Generated @context with prefixes: {list(context.keys())}")
                
                logger.info(f"Successfully converted {file_ext} to JSON-LD")
                
            except Exception as e:
                logger.error(f"Error parsing {file_ext} file: {e}")
                raise
                
        elif file_ext == '.json' or file_ext == '.jsonld':
            # Load JSON-LD directly
            with open(ontology_path, 'r') as f:
                self.ontology = json.load(f)
            logger.info(f"Loaded JSON-LD ontology from {ontology_path}")
        else:
            raise ValueError(f"Unsupported file format: {file_ext}. Supported formats: .ttl, .rdf, .owl, .n3, .nt, .json, .jsonld")
        
        logger.info(f"Ontology loaded with {len(self.ontology)} top-level elements")
    
    def get_context_from_ontology(self) -> str:
        """Extract or generate context definition from loaded ontology"""
        if not self.ontology:
            logger.warning("No ontology loaded")
            return "{}"
        
        context = {}
        
        # If ontology has @context, use it
        if '@context' in self.ontology:
            context = self.ontology['@context']
        
        # Convert to string format for prompts
        context_str = json.dumps({"@context": context}, indent=2)
        return context_str
        
    def create_ontology_mapping_prompt(self, context_definition: str, data: str) -> str:
        """Create prompt for ontology mapping"""
        return f"""Here is a context definition for the ontology:
Context Definition:
{context_definition}
---------
Generate a JSON-LD using the following data and the above context definition.
Use '@graph' object namespace for the data in JSON-LD.
Be comprehensive and make sure to fill all of the data.
Keep nesting to the minimum and still be able to disambiguate.
If there are multiple subfields enumerated in a 'List' namespace then do not combine them in a single subfield, keep them as separate subfields to disambiguate.
Ensure that you populate all items in the 'List' namespace, do not leave any item.
Do not include any explanations or apologies in your response.
Do not add any other text other than the generated JSON-LD in your response.
Generate in JSON format.
---------
Data:
{data}
---------
JSON-LD json:"""

    def map_documents_to_ontology(self, 
                                  documents: List[str], 
                                  context_definition: str) -> List[Dict]:
        """Map documents to ontology using LLM"""
        mapped_data = []
        
        for i, doc in enumerate(documents):
            logger.info(f"Mapping document {i+1}/{len(documents)} to ontology...")
            prompt = self.create_ontology_mapping_prompt(context_definition, doc)
            response = self.llm.generate(prompt)
            
            try:
                # Extract JSON from response
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                if json_start != -1 and json_end != 0:
                    json_str = response[json_start:json_end]
                    json_data = json.loads(json_str)
                    mapped_data.append(json_data)
                    logger.info(f"Successfully mapped document {i+1}")
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse JSON from LLM response for document {i+1}: {e}")
                
        return mapped_data

    def flatten_factual_block(self, 
                              factual_block: Dict, 
                              prefix: str = "") -> List[Tuple[str, str]]:
        """Flatten nested factual blocks into key-value pairs"""
        flattened = []
        
        def _flatten(obj, current_prefix):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key.startswith('@'):  # Skip JSON-LD metadata
                        continue
                    new_prefix = f"{current_prefix} {key}".strip() if current_prefix else key
                    if isinstance(value, (dict, list)):
                        _flatten(value, new_prefix)
                    else:
                        flattened.append((new_prefix, str(value)))
            elif isinstance(obj, list):
                for item in obj:
                    _flatten(item, current_prefix)
                    
        _flatten(factual_block, prefix)
        return flattened

    def construct_hypergraph(self, ontology_mapped_data: List[Dict]):
        """Construct hypergraph from ontology-mapped data"""
        self.hypernodes.clear()
        self.hyperedges.clear()
        
        logger.info("Constructing hypergraph...")
        
        for data_idx, data in enumerate(ontology_mapped_data):
            # Handle @graph structure if present
            if '@graph' in data:
                graphs = data['@graph'] if isinstance(data['@graph'], list) else [data['@graph']]
            else:
                graphs = [data]
                
            for graph in graphs:
                # Flatten the factual block
                flattened_facts = self.flatten_factual_block(graph)
                
                if not flattened_facts:
                    continue
                
                # Create hypernodes
                hyperedge_nodes = set()
                for key, value in flattened_facts:
                    node_id = f"{key}:{value}"
                    if node_id not in self.hypernodes:
                        embedding = self.embedder.encode(f"{key} {value}")
                        self.hypernodes[node_id] = Hypernode(key, value, embedding)
                    hyperedge_nodes.add(node_id)
                
                # Create hyperedge if we have multiple nodes
                if len(hyperedge_nodes) > 1:
                    fact_text = " AND ".join([f"{self.hypernodes[n].key} = {self.hypernodes[n].value}" 
                                             for n in hyperedge_nodes])
                    self.hyperedges.append(Hyperedge(hyperedge_nodes, fact_text))
        
        logger.info(f"Created {len(self.hypernodes)} hypernodes and {len(self.hyperedges)} hyperedges")

    def retrieve_relevant_nodes(self, 
                                query: str, 
                                k: int = 5) -> Tuple[Set[str], Set[str]]:
        """Retrieve relevant hypernodes for a query"""
        query_embedding = self.embedder.encode(query)
        
        # Calculate similarities for keys and values
        key_similarities = []
        value_similarities = []
        
        for node_id, node in self.hypernodes.items():
            # Similarity with key
            key_embedding = self.embedder.encode(node.key)
            key_sim = cosine_similarity([query_embedding], [key_embedding])[0][0]
            key_similarities.append((node_id, key_sim))
            
            # Similarity with value
            value_sim = cosine_similarity([query_embedding], [node.embedding])[0][0]
            value_similarities.append((node_id, value_sim))
        
        # Get top-k nodes for each
        key_similarities.sort(key=lambda x: x[1], reverse=True)
        value_similarities.sort(key=lambda x: x[1], reverse=True)
        
        ns_q = {node_id for node_id, _ in key_similarities[:k]}
        nv_q = {node_id for node_id, _ in value_similarities[:k]}
        
        return ns_q, nv_q

    def retrieve_context(self, 
                         query: str, 
                         k: int = 5,
                         max_hyperedges: int = 10) -> List[str]:
        """Retrieve relevant context for a query using greedy hyperedge selection"""
        # Get relevant nodes
        ns_q, nv_q = self.retrieve_relevant_nodes(query, k=k)
        relevant_nodes = ns_q.union(nv_q)
        
        # Find hyperedges that cover the most relevant nodes (greedy algorithm)
        context_hyperedges = []
        covered_nodes = set()
        
        while relevant_nodes - covered_nodes and len(context_hyperedges) < max_hyperedges:
            best_edge = None
            best_coverage = 0
            
            for edge in self.hyperedges:
                uncovered = edge.nodes.intersection(relevant_nodes - covered_nodes)
                if len(uncovered) > best_coverage:
                    best_edge = edge
                    best_coverage = len(uncovered)
            
            if best_edge:
                context_hyperedges.append(best_edge)
                covered_nodes.update(best_edge.nodes)
            else:
                break
        
        # Convert hyperedges to context strings
        context = []
        for edge in context_hyperedges:
            facts = []
            for node_id in edge.nodes:
                node = self.hypernodes[node_id]
                facts.append(f"{node.key}: {node.value}")
            context.append("\n".join(facts))
        
        return context

    def generate_response(self, query: str, context: List[str]) -> str:
        """Generate response using retrieved context"""
        context_str = "\n\n".join(context)
        prompt = f"""Given the context below, generate the answer to the given query. 
Note that the context is provided as a list of valid facts in a dictionary format.

Context:
{context_str}

Query: {query}

Answer:"""
        
        return self.llm.generate(prompt, temperature=0.1)

    def query(self, query: str, k: int = 5, max_hyperedges: int = 10) -> Dict[str, Any]:
        """Main query interface"""
        # Retrieve context
        context = self.retrieve_context(query, k=k, max_hyperedges=max_hyperedges)
        
        # Generate response
        response = self.generate_response(query, context)
        
        return {
            "query": query,
            "context": context,
            "response": response
        }

    def split_document(self, text: str, max_tokens: int = 2000) -> List[str]:
        """Split document into chunks"""
        # Simple splitting by paragraphs
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = ""
        
        for para in paragraphs:
            # Rough token estimation (1 token ≈ 4 characters)
            if len(current_chunk) + len(para) < max_tokens * 4:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks

    def save_hypergraph(self, path: str):
        """Save hypergraph to disk"""
        with open(path, 'wb') as f:
            pickle.dump({
                'hypernodes': self.hypernodes,
                'hyperedges': self.hyperedges,
                'ontology': self.ontology
            }, f)
        logger.info(f"Saved hypergraph to {path}")

    def load_hypergraph(self, path: str):
        """Load hypergraph from disk"""
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.hypernodes = data['hypernodes']
            self.hyperedges = data['hyperedges']
            self.ontology = data.get('ontology', {})
        logger.info(f"Loaded hypergraph from {path}")
