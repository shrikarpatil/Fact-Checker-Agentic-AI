import socketio
from socketConfig import sio
from agent import agent
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

appAsgi = socketio.ASGIApp(sio, other_asgi_app=app)
class ClaimRequest(BaseModel):
    claim: str

@app.post("/fact-check")
async def fact_check(request:ClaimRequest):   
    initial_state = {"claim": request.claim}
    result =   await agent.ainvoke(initial_state)   
    verdict = result.get("verdict") 
    return {
        "claim": request.claim,
        "verdict": verdict.content,
        "searchResults": result.get("searchResults", "N/A")
    }
