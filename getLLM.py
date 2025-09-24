import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

load_dotenv()

llm_mode = os.getenv("LLM_MODE", "local")

def getLLM():
    api_key = os.getenv("OLLAMA_API_KEY")
    api_endpoint = os.getenv("OLLAMA_API_ENDPOINT", "https://ollama.com")
    llm = OllamaLLM(model="llama3", api_key=api_key, api_endpoint=api_endpoint)
    print(f"Using {llm_mode} LLM")
    return llm

