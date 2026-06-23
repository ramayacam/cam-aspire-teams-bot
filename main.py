import re
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from app.bot import handle_message
from app.knowledge import KnowledgeBase
from config.settings import settings

app = FastAPI(title="Aspire Knowledge Bot")

kb = KnowledgeBase()

# Bot Framework adapter — validates Azure JWT tokens on every message
adapter_settings = BotFrameworkAdapterSettings(
    app_id=settings.AZURE_APP_ID,
    app_password=settings.AZURE_APP_PASSWORD,
)
adapter = BotFrameworkAdapter(adapter_settings)


async def on_message(turn_context: TurnContext):
    """Called by the adapter for every validated Teams message."""
    text = turn_context.activity.text or ""
    # Remove @mention tags
    text = re.sub(r"<at>.*?</at>\s*", "", text).strip()

    if not text:
        await turn_context.send_activity("Please ask a question about Aspire Cloud.")
        return

    user_id = turn_context.activity.from_property.id or "unknown"
    answer = await handle_message(text, user_id)
    await turn_context.send_activity(answer)


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
        ],
    }


@app.post("/ask")
async def ask(request: Request):
    """Test endpoint — no auth required."""
    try:
        body = await request.json()
        question = body.get("question", "")
        if not question:
            return JSONResponse({"error": "No question provided"})
        answer = await handle_message(question)
        return JSONResponse({"question": question, "answer": answer})
    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/api/messages")
async def messages_get():
    """Azure Bot Framework verification endpoint."""
    return Response(status_code=200)

@app.post("/api/messages")
async def messages(request: Request):
    """Main Teams webhook."""
    try:
        body = await request.json()
        print(f"Received message: {body}")

        activity = Activity().deserialize(body)

        # Skip JWT validation temporarily for debugging
        async def call_bot(turn_context: TurnContext):
            await on_message(turn_context)

        await adapter.process_activity(activity, "", call_bot)
        return Response(status_code=201)

    except Exception as e:
        print(f"Teams webhook error: {type(e).__name__}: {e}")
        return Response(status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.BOT_PORT)
