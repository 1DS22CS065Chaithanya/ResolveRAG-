from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from embeddings import get_embedding_model
from prompts import SYSTEM_PROMPT

VECTOR_DB_PATH = "vector_store"

def get_rag_answer(question: str, k: int = 4):
    # 1. Load embedding model
    embedding = get_embedding_model()

    # 2. Load vector store
    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embedding,
        allow_dangerous_deserialization=True
    )

    # 3. Retrieve relevant chunks
    docs = vectorstore.similarity_search(question, k=k)

    context = "\n\n".join(
        f"Source: {doc.metadata.get('source')}\n{doc.page_content}"
        for doc in docs
    )

    # 4. Load Ollama LLM (CORRECT CLASS)
    llm = OllamaLLM(model="llama3")

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer:
"""

    # ✅ CORRECT WAY TO CALL THE LLM
    response = llm.invoke(prompt)

    return response, docs
