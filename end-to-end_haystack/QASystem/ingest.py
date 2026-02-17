from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path
from QASystem.utils import pinecone_config
 
 
 
def ingest(document_store):
    indexing = Pipeline()

    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(
        split_by="word",
        split_length=200,       
        split_overlap=50  
    ))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))
    
    # connecting component
    indexing.connect("converter","splitter")
    indexing.connect("splitter","embedder")
    indexing.connect("embedder","writer")

    # indexing.run({"converter": {"sources": [Path("D:\\Machine Learing\\end-to-end_haystack\\data\\RAG research paper.pdf")]}})
    indexing.run({
    "converter": {
        "sources": [str(Path(r"D:\Machine Learing\end-to-end_haystack\data\RAG research paper.pdf"))]
    }
})


if __name__ == '__main__':
    document_store = pinecone_config()
    ingest(document_store)