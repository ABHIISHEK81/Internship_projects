from fastapi import FastAPI
from pydantic import BaseModel

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from src.retriever import get_retriever
from src.pipeline import run_pipeline

class UserInput(BaseModel):
    query: str
    completed_courses: list | None = None
    target_program: str | None = None
    term: str | None = None

app = FastAPI()

@app.post("/plan")
def generate_plan_api(user_input: UserInput):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.load_local(
        "faiss_index", 
        embedding_model, 
        allow_dangerous_deserialization=True
    )
    retriever = get_retriever(vectorstore)
    llm = OllamaLLM(model="llama3.1")
    
    return run_pipeline(
        llm=llm,
        retriever=retriever,
        user_input=user_input.dict()
    )
