from src.ingestion import load_documents
from src.chunking import chunk_documents
from src.embeddings import build_vector_store
from src.retriever import get_retriever

urls = [
    "https://en.wikipedia.org/wiki/Computer_science",
    "https://en.wikipedia.org/wiki/List_of_computer_scientists"
]

docs = load_documents(urls)
chunks = chunk_documents(docs)
vectorstore = build_vector_store(chunks)
retriever = get_retriever(vectorstore)

vectorstore.save_local("faiss_index")

print("Index built successfully - saved to faiss_index")
