from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

# Load embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

# Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# LLM (LLaMA 3)
llm = Ollama(model="llama3")

# RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

# Ask question
query = "What is RAG and why is it useful?"
response = qa_chain.invoke({"query":query})

print(response)
print(response["result"])