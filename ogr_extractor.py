from pathlib import Path
import json
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF
import ollama
import hashlib


# === Configuration ===
ONTOLOGY_PATH = "sws.ttl"
DOCS_DIR = "docs"
OUTPUT_TTL_PATH = "domain_specific_ontology.ttl"
NAMESPACE_URI = "http://www.sws.org/sws#"
MODEL_NAME = "mistral"

# === Load Ontology ===
def load_ontology_terms(ttl_path):
    g = Graph()
    g.parse(ttl_path, format="ttl")
    terms = set()
    for s in g.subjects(RDF.type, None):
        terms.add(s.split("#")[-1] if "#" in s else str(s))
    return list(terms)

# === Call Ollama to Extract Factual Blocks ===
def extract_factual_blocks(doc_text, ontology_terms):
    terms_str = ", ".join(ontology_terms)
    prompt = f"""
You are given a project document and a set of ontology terms.
Extract factual blocks as subject-attribute-value triplets grounded in the ontology vocabulary.

Ontology Terms:
{terms_str}

Document:
{doc_text[:4000]}

Respond only in this JSON format:
[
  {{ "subject": "...", "attribute": "...", "value": "..." }},
  ...
]
"""
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    print(f"Response: {response}")
    try:
        return json.loads(response["message"]["content"])
    except Exception:
        return []

# === Flatten to Hyperedges ===
def flatten_to_hyperedges(factual_blocks):
    return [[(f"{f['subject']} ⊕ {f['attribute']}", f["value"])] for f in factual_blocks]

# === Build Hypergraph ===
class Hypergraph:
    def __init__(self):
        self.hypernodes = set()
        self.hyperedges = []

    def add_edge(self, edge):
        self.hyperedges.append(edge)
        for node in edge:
            self.hypernodes.add(node)

# === Generate Unique URI for String ===
def uri_from_string(s):
    return URIRef(NAMESPACE_URI + hashlib.md5(s.encode()).hexdigest())

# === Write Triples to RDF Graph ===
def write_triples_to_graph(hypergraph):
    ns = Namespace(NAMESPACE_URI)
    g = Graph()
    g.bind("ind", ns)

    for edge in hypergraph.hyperedges:
        for (key, value) in edge:
            subj_pred = key.split(" ⊕ ")
            if len(subj_pred) == 2:
                s, p = subj_pred
                s_uri = uri_from_string(s)
                p_uri = uri_from_string(p)
                o = Literal(value) if not value.istitle() else uri_from_string(value)
                g.add((s_uri, p_uri, o))
    return g

# === Main Execution ===
def run_pipeline():
    ontology_terms = load_ontology_terms(ONTOLOGY_PATH)
    hg = Hypergraph()

    for file_path in Path(DOCS_DIR).glob("*.txt"):
        doc_text = file_path.read_text(encoding="utf-8")
        blocks = extract_factual_blocks(doc_text, ontology_terms)
        edges = flatten_to_hyperedges(blocks)
        for edge in edges:
            hg.add_edge(edge)

    rdf_graph = write_triples_to_graph(hg)
    rdf_graph.serialize(destination=OUTPUT_TTL_PATH, format="ttl")
    return f"✅ Domain ontology written to {OUTPUT_TTL_PATH}"

# Run it
if __name__ == "__main__":
    print(run_pipeline())
