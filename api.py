from agent import agent
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ClaimRequest(BaseModel):
    claim: str

@app.post("/fact-check")
async def fact_check(request:ClaimRequest):
    initial_state = {"claim": request.claim}
    result = agent.invoke(initial_state)
    return {
        "claim": request.claim,
        "verdict": result["verdict"],
        "searchResults": result.get("searchResults", "N/A")
    }
   