import os
import streamlit as st
from ingest import ingest_file
from rag import get_rag_chain


UPLOAD_DIR = "data/uploaded_files"
os.makedirs(UPLOAD_DIR,exist_ok=True)

st.set_page_config(page_title="RAG AI Assistant",layout="wide")

st.title ("RAG AI Assistant")
st.write("PDF QA")

mode = st.sidebar.selectbox(
    "Select Mode",
    ["PDF Question Answering","CV Analyzer","Notes QA Bot"]
)
uploaded_file = st.file_uploader(
    "Upload PDF or Text file",
    type=["pdf","txt"]
)
if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR,uploaded_file.name)
    with open(file_path,"wb") as f:
        f.write(uploaded_file.read())
    
    if st.button("ingest document"):
        with st.spinner("Ingesting document"):
            ingest_file(file_path)
        st.success("Document ingested success")
st.divider()

query = st.text_input("Ask your question")

if st.button("Get answer"):
    if not query:
        st.warning("please enter a question")
    else:
        with st.spinner("Thinking..."):
            qa_chain = get_rag_chain()
            if mode == "CV Analyzer":
                query = f"""Analyze the resume and answer:
                1. Strengths
                2. Weakness
                3. Missing skills 
                Resume Question: {query}
            """
            response = qa_chain.invoke({"query": query})
            st.subheader("Answer")
            st.write(response["result"])