from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_documents(folder_path: str):
    # Load all PDFs in the specified folder
    loader = PyPDFLoader(folder_path)
    documents = loader.load()
    return documents

def create_vector_store(documents):
    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store

