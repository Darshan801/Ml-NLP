from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from haystack.utils import Secret 
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

#setting env vairable
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['HF_API_TOKEN'] = HF_API_TOKEN
    
print("Import Successfully")

def pinecone_config():
    #configuring pinecone database
    document_store = PineconeDocumentStore(
        api_key=Secret.from_token(PINECONE_API_KEY),
            namespace="default",
            index="haystack-new-768",  # New index name
            dimension=768,  # Matches your 768-dim model
            spec={
            "serverless": {
                "cloud": "aws",
                "region": "us-east-1"
            }
        }
        )
    return document_store

 
