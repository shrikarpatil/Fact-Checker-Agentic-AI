import os
from typing import TypedDict
from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph,START,END
from tavily import TavilyClient
from dotenv import load_dotenv
from getLLM import getLLM
from socketConfig import sio

load_dotenv()
apiKey = os.getenv("TAVILY_API_KEY")
llm = getLLM()
tavilyClient = TavilyClient(api_key=apiKey)


class State (TypedDict):
    claim : str
    searchResults : dict
    verdict : str

graph = StateGraph(State)

async def webSearch(state : dict) -> dict:
    await sio.emit("status", {"message": "🔍 Performing web search..."})
    claim = state["claim"]
    results = tavilyClient.search(query=claim, max_results=5, search_depth="advanced")
    formatted_results = "\n\n".join(
        [f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content']}" for r in results["results"]]
    )
    state["searchResults"] = formatted_results
    await sio.emit("status", {"message": "✅ Web search completed"})
    return state


async def verifyClaim(state : dict) -> dict:   
    await sio.emit("status", {"message": "🤖 Verifying claim..."})
    claim = state["claim"]
    searchResults = state["searchResults"]
    prompt = f"""
    You are a fact-checking AI. Your task is to verify the truthfulness of a given claim based on provided web search results. 
    Carefully analyze the search results and determine whether they support, refute, or are insufficient to verify the claim.

    Claim: "{claim}"

    Web Search Results:
    {searchResults}

    Instructions:
    1. If the search results provide clear evidence supporting the claim, respond with "True".
    2. If the search results provide clear evidence refuting the claim, respond with "False".
    3. If the search results are inconclusive or do not provide enough information to verify the claim, respond with "Uncertain".
    4. Provide a brief explanation for your conclusion based on the search results.

    Response Format:
    - Your response should be in the following format:
      Conclusion: [True/False/Uncertain]
      Explanation: [Your brief explanation here]

    Example Responses:
    - Conclusion: True
      Explanation: The search results include multiple credible sources confirming the claim.

    - Conclusion: False
      Explanation: The search results include credible sources that directly contradict the claim.

    - Conclusion: Uncertain
      Explanation: The search results do not provide enough information to verify the claim.
    
    Now, please analyze the claim and the search results to provide your conclusion.
    """
    response = await llm.ainvoke(prompt)    
    state["verdict"] = response   
    await sio.emit("status", {"message": "🎉 Verification completed"})
    return state

graph.add_node("webSearch", webSearch)
graph.add_node("verifyClaim", verifyClaim)

graph.add_edge(START, "webSearch")
graph.add_edge("webSearch", "verifyClaim")
graph.add_edge("verifyClaim", END)

agent = graph.compile()
   
