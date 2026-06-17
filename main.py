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
    return {
        "total_chunks": len(kb.chunks),
        "sources": list(set(c["source"] for c in kb.chunks)) if kb.chunks else [],
    }


@app.get("/debug/search")
async def debug_search(q: str = "complete work ticket"):
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
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.post("/api/messages")
async def teams_webhook(request: Request):
    """Handles Teams Outgoing Webhook messages"""
    try:
        body = await request.json()

        # Extract text and remove bot @mention
        text = body.get("text", "")
        text = re.sub(r'<at>.*?</at>\s*', '', text).strip()

        if not text:
            return JSONResponse({
                "type": "message",
                "text": "Please ask a question about Aspire Cloud."
            })

        # Get user info
        user_id = body.get("from", {}).get("id", "unknown")

        # Process with RAG
        response = await handle_message(text, user_id)

        return JSONResponse({
            "type": "message",
            "text": response
        })

    except Exception as e:
        print(f"Teams webhook error: {str(e)}")
        return JSONResponse({
            "type": "message",
            "text": "Something went wrong. Please try again."
        })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.BOT_PORT)
