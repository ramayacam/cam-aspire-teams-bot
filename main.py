import re
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.bot import handle_message
from app.knowledge import KnowledgeBase
from config.settings import settings

app = FastAPI(title="Aspire Knowledge Bot")

kb = KnowledgeBase()


@app.get("/health")
async def health():
    return {"status": "ok", "message": "Bot is running"}


@app.get("/")
async def root():
    return {"message": "Aspire Knowledge Bot API"}


@app.get("/debug")
async def debug():
    return kb.stats()


@app.get("/debug/search")
async def debug_search(q: str = "complete work ticket"):
    results = kb.search(q, top_k=6)
    return {
        "query": q,
        "results_found": len(results),
        "results": [
            {"source": r["source"], "header": r["header"], "preview": r["content"][:200]}
            for r in results
        ]
    }


@app.post("/ask")
async def ask(request: Request):
    try:
        body = await request.json()
        question = body.get("question", "")
        if not question:
            return JSONResponse({"error": "No question provided"})
        response = await
