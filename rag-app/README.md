# RAG-Based Question Answering System free

This project implements a **Retrieval-Augmented Generation (RAG)** application using
 free and open source tools
It allows users to ask questions over their own documents and receive
**grounded, context-aware answers**.

## RAG Architecture
Documents-> Chunking -> Embeddings ->Vector DB -> UserQuery -> Embedding -> similarity search -> retrieved context-> LLM -> Answer

## Features
- Document ingestion and chunking
- Semantic search using vector embeddings
- Local vector database (ChromaDB)
- Local LLM inference using Ollama (LLaMA 3)
- Reduced hallucinations via retrieval grounding

---

##  Tech Stack
| Component | Tool |
| Language | Python |
| Embeddings | sentence-transformers (MiniLM) |
| Vector DB | ChromaDB (local) |
| LLM | LLaMA 3 (via Ollama) |
| Framework | LangChain |

