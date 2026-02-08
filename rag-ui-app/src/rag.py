from langchain_ollama import OllamaLLM
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
def get_rag_chain(persist_dir = "chroma_db"):
    embeddings = HuggingFaceEmbeddings(
        model_name = EMBEDDING_MODEL
    )
    db = Chroma(
        persist_directory= persist_dir,
        embedding_function=embeddings
    )
    retriever = db.as_retriever(search_kwargs={"k":3})
    llm = OllamaLLM(
        model = "llama3",
        temperature = 0,
        
    )
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
         verbose=False
    )
    return qa