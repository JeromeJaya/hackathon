from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS

def create_pipeline(vector_store):
    retriever = vector_store.as_retriever()
    chat_model = ChatOpenAI()  # Replace with NVIDIA wrapper if necessary
    chain = ConversationalRetrievalChain.from_llm(llm=chat_model, retriever=retriever)
    return chain
