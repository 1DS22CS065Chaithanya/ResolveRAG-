from fastapi import FastAPI
from pydantic import BaseModel
from rag_chain import get_rag_answer

app = FastAPI(title="Service Desk RAG API")

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query_rag(request: QueryRequest):
    answer, sources = get_rag_answer(request.question)

    return {
        "answer": answer,
        "sources": [
            {
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page")
            }
            for doc in sources
        ]
    }
