from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings

DB_PATH = "vectorstore"

def get_retriever():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever(search_kwargs={"k": 3})