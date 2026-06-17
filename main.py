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
    """Shows how many docs and chunks are loaded"""
    return {
        "total_chunks": len(kb.chunks),
        "sources": list(set(c["source"] for c in kb.chunks)) if kb.chunks else [],
        "sample": kb.chunks[0]["content"][:200] if kb.chunks else "No chunks loaded"
    }


@app.get("/debug/search")
async def debug_search(q: str = "complete work ticket"):
    """Test search results"""
    results = kb.search(q, top_k=3)
    return {
        "query": q,
        "results_found": len(results),
        "results": [
            {"source": r["source"], "preview": r["content"][:300]}
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

        response = await handle_message(question)

        return JSONResponse({
            "question": question,
            "answer": response
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.post("/api/messages")
async def messages(request: Request):
    try:
        body = await request.json()
        text = body.get("text", "")

        if not text:
            return JSONResponse({"error": "No message text"})

        response = await handle_message(text)

        return JSONResponse({
            "type": "message",
            "text": response
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.BOT_PORT)
