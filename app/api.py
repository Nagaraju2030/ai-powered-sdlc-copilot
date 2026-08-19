from fastapi import FastAPI
from pydantic import BaseModel, Field
from .graph import sdlc_graph

app = FastAPI(title="AI-Powered SDLC Copilot", version="1.0.0")

class SDLCRequest(BaseModel):
    requirement: str = Field(min_length=20, max_length=20000)
    approved: bool = False

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(request: SDLCRequest):
    return sdlc_graph.invoke(request.model_dump())
