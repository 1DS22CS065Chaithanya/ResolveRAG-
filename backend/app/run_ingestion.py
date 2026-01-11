from ingest import load_pdfs
from chunking import chunk_documents
from vector_store import create_vector_store

def run():
    docs = load_pdfs()
    print(f"Loaded {len(docs)} pages")

    chunks = chunk_documents(docs)
    print(f"Created {len(chunks)} chunks")

    create_vector_store(chunks)
    print("Vector store created successfully")

if __name__ == "__main__":
    run()
