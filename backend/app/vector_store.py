from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from embeddings import get_embedding_model

VECTOR_DB_PATH = "vector_store"

def create_vector_store(chunks: list[Document]):
    embedding = get_embedding_model()
    vectorstore = FAISS.from_documents(chunks, embedding)
    vectorstore.save_local(VECTOR_DB_PATH)
    return vectorstore
