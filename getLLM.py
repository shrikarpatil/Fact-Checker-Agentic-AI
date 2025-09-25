import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

load_dotenv()

def getLLM():
    api_key = os.getenv("OLLAMA_API_KEY")
    api_endpoint = os.getenv("OLLAMA_API_ENDPOINT")
    llm = OllamaLLM(model="llama3", host=api_endpoint)   
    return llm

