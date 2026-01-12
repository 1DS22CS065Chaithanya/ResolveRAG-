# from fastapi import FastAPI
# from pydantic import BaseModel
# from rag_chain import get_rag_answer

# app = FastAPI(title="Service Desk RAG API")

# class QueryRequest(BaseModel):
#     question: str

# @app.post("/query")
# def query_rag(request: QueryRequest):
#     answer, sources = get_rag_answer(request.question)

#     return {
#         "answer": answer,
#         "sources": [
#             {
#                 "source": doc.metadata.get("source"),
#                 "page": doc.metadata.get("page")
#             }
#             for doc in sources
#         ]
#     }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_chain import get_rag_answer

app = FastAPI(title="Service Desk RAG API")

# 🔹 CORS CONFIGURATION (REQUIRED FOR FRONTEND)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
                "page": doc.metadata.get("page"),
            }
            for doc in sources
        ],
    }
