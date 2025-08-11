from ograg_ollama import OGRAG

# Initialize OG-RAG
ograg = OGRAG(llm_model="mistral:latest")

# Load your ontology (supports multiple formats)
ograg.load_ontology("sws.ttl")    # Turtle format
# ograg.load_ontology("your_ontology.rdf")  # RDF/XML format
# ograg.load_ontology("your_ontology.owl")  # OWL format
# ograg.load_ontology("your_ontology.json") # JSON-LD format

# Get context definition from loaded ontology
context_definition = ograg.get_context_from_ontology()

# Or define your own context based on your ontology
# context_definition = """
# @context: {
#     "YourDomain": "http://yourdomain.org/ontology#",
#     "hasProperty": "YourDomain:hasProperty",
#     "relatesTo": "YourDomain:relatesTo"
#     # Add your ontology terms here
# }
# """

# Load and process documents
with open("swsmd.md", "r", encoding="utf-8") as f:
    document_text = f.read()

# Split large documents
documents = ograg.split_document(document_text)

# Map documents to ontology
mapped_data = ograg.map_documents_to_ontology(documents, context_definition)

# Build hypergraph
ograg.construct_hypergraph(mapped_data)

# Save for later use
ograg.save_hypergraph("my_knowledge_graph.pkl")

# Query the system
result = ograg.query("who are the HumanActors in manufacturing pilot?")
print(result['response'])