## RAG Document Question-Answering

A Retrieval-Augmented Generation (RAG) system for answering questions from PDF documents using vector and LLM 
This project uses Sentence Transformers for embeddings, FAISS for fast similarity search, and Ollama to generate answers based on retrieved context.

---

## Features

- Load and preprocess PDF documents
- Split text into overlapping chunks for better retrieval
- Embed chunks using Sentence Transformers
- Build a FAISS vector store for fast similarity search
- Retrieve relevant chunks based on user questions
- Generate answers grounded in the retrieved context
- Command-line interface for easy interaction



## Requirements

- Python 3.10+
- Install dependencies:


