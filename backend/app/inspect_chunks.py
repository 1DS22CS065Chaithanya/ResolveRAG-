from langchain_community.vectorstores import FAISS
from embeddings import get_embedding_model
from pathlib import Path

VECTOR_DB_PATH = "vector_store"

def inspect_chunks(limit=5):
    embedding = get_embedding_model()

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embedding,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.docstore._dict.values()

    print(f"Total chunks stored: {len(docs)}\n")

    for i, doc in enumerate(docs):
        print(f"--- CHUNK {i+1} ---")
        print("SOURCE:", doc.metadata.get("source"))
        print("PAGE:", doc.metadata.get("page"))
        print("TEXT:")
        print(doc.page_content[:800])  # first 800 chars
        print("\n")

        if i + 1 >= limit:
            break

if __name__ == "__main__":
    inspect_chunks(limit=5)
