from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

PDF_DIR = Path("data/pdfs")

def load_pdfs() -> list[Document]:
    documents = []

    for pdf_file in PDF_DIR.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        pages = loader.load()

        for page in pages:
            page.metadata["source"] = pdf_file.name
            documents.append(page)

    return documents
