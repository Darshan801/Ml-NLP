import subprocess
from ingest import load_pdf , chunk_text
from vector_store import create_vector_store
from rag_pipeline import retrieve
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

text = load_pdf("../data/RAG research paper.pdf")
chunks = chunk_text(text)

index , stored_chunks= create_vector_store(chunks)

question = input("Ask a question: ")

context = retrieve(question , index , stored_chunks , EMBEDDING_MODEL)

prompt = f"""
You are a research assistant.

Using the context below, explain the concept asked in the question.
If the context provides a definition, restate it clearly in your own words.
If multiple aspects are mentioned, summarize them concisely.
Do not use information outside the context.

Context:
{context}

Question:
{question}

"""
# print("\n--- RETRIEVED CONTEXT ---\n")
# print(context)
# print("\n------------------------\n")

result = subprocess.run(
    ["ollama","run","llama3"],
    input=prompt,
    text=True,
    encoding="utf-8", # outout it it can cause charmap' codec can't encode character '\ufb01'
    capture_output=True
)
print("\nAnswer:\n",result.stdout)