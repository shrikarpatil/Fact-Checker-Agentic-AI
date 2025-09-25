import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def getLLM():
     api_key = os.getenv("API_KEY")
     llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
        temperature=0.7
    )
     return llm

