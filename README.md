Implemented RAG chatbot in local system to learn from pdf [just like chatgpt but customized for my data]
Gathered doc/pdf where I wish to understand 

requirements involved in this 
RAG 
vector db[localstorge]
langchain and its sub modules 
Local storage of > 20 GB 
OLLAMA embeddings 
Streamlit[host]

Here is what I did 
Installed all the requirements 
PDF is split to embeddings and stored as vector data folder using python[ingest.py]
Another file to read the data present in vector data[retriever.py] [i can say kind of mapping info]


Outcome:
When I ask a question  related to pdf I fed to LLM , [it maps meaning internally as per meaning as data will be stored In numeric form in vector data ] , it gives answer as per my query[outcome speed varies on laptop model]

