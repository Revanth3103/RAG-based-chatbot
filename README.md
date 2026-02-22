Implemented RAG chatbot in local system to learn from pdf [just like chatgpt but customized for my data]
Gathered doc/pdf where I wish to understand 

requirements involved in this 
RAG 
vector db[localstorge]
langchain and its sub modules 
Local storage of > 20 GB 
OLLAMA embeddings 
Streamlit[host]

Here is what I did: 
Installed all the requirements 
PDF is split to embeddings and stored as vector data folder using python[ingest.py]
Another file to read the data present in vector data[retriever.py] [i can say kind of mapping info]

<img width="271" height="295" alt="image" src="https://github.com/user-attachments/assets/cc7e6bd3-b0ed-4582-b0a9-a5be80769aa9" />



Outcome:
When I ask a question  related to pdf I fed to LLM , [it maps meaning internally as per meaning as data will be stored In numeric form in vector data ] , it gives answer as per my query[outcome speed varies on laptop model]

STEPS TO IMPLEMENT :

INSTALL AND IMPORT REQUIRED LIBRARIES 
CREATE VENV 
USE ingest.py file to convert data to embeddings [pdf file should be stored in data folder]
After runing ingest.py you will get vectorbase folder , it consists 2 files index.faiss and index.pkl
USE retriever.py to convert embeddings to human language 
Add code app.py where the information is retrieved and stored
After vectorbase is generated , give command streamlit run app.py 
Using STreamlit it will open outcome in localhost:8501 

You can query anything in the search box related to pdf/doc you uploaded. The response time varies from one machine to other.

