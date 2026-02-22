import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from retriever import get_retriever

st.title("RAG Chatbot")

query = st.text_input("Ask a question")

if query:
    llm = Ollama(model="mistral")
    retriever = get_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    response = qa.run(query)
    st.write(response)