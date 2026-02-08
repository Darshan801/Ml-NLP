import os
from langchain_community.document_loaders import PyPDFLoader , TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def ingest_file(file_path , persist_dir = "chroma_db"):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 100
    )
    chunks = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(
        model_name = EMBEDDING_MODEL
    )
    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory=persist_dir
    )
    return db
# ingest_file("../data/docs.txt")