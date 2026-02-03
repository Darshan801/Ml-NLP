# Implementing Retrieval-augmented generation(RAG)

## Project Overview
This project focuses on creating RAG pipeline 

This project uses  counter approach to calculate the cosec similarites between user_input , and relevant-document

Cosec_similirities = A.B / |A|*|B|

## Structure
- `src/` – RAG-implementation notebook
- `data/` – dataset files
- `venv/` – virtual environment (ignored)

## Technologies
- Python
- Pandas
- LLAMA2 (model)
- Git & GitHub

## Results
- Configured LLAMA in our local system 
- successfully generated a response using LLAMA model

## How to Run
```bash
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
python src/RAG-implemetation.ipynb