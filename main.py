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

# Bot Framework adapter — configured for a Single Tenant Azure Bot.
# Single Tenant bots authenticate against their specific tenant, not the
# global endpoint. We pass channel_auth_tenant + custom app_credentials so
# tokens are validated against login.microsoftonline.com/<tenant>.
from botframework.connector.auth import MicrosoftAppCredentials

app_credentials = MicrosoftAppCredentials(
    settings.AZURE_APP_ID,
    settings.AZURE_APP_PASSWORD,
    channel_auth_tenant=settings.AZURE_TENANT_ID,
)
adapter_settings = BotFrameworkAdapterSettings(
    app_id=settings.AZURE_APP_ID,
    app_password=settings.AZURE_APP_PASSWORD,
    channel_auth_tenant=settings.AZURE_TENANT_ID,
    app_credentials=app_credentials,
)
adapter = BotFrameworkAdapter(adapter_settings)


async def on_message(turn_context: TurnContext):
    """Called by the adapter for every incoming activity."""
    # Only respond to actual text messages. Teams also sends system events
    # (members added, conversation updates, typing, etc.) — ignore those
    # so the bot doesn't reply with the default prompt repeatedly.
    if turn_context.activity.type != "message":
        return

    text = turn_context.activity.text or ""
    text = re.sub(r"<at>.*?</at>\s*", "", text).strip()

    if not text:
        return  # empty message, nothing to answer

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


@app.get("/debug/tokens")
async def debug_tokens(q: str = "How do I complete a work ticket?"):
    """Diagnostic: shows how many chunks are retrieved for a query and an
    estimate of the tokens sent to Claude. Useful for tuning and cost analysis.
    Token estimate uses the chars/4 heuristic (close to real Claude tokens
    for English markdown)."""
    chunks = kb.search(q, top_k=6)

    context_text = "\n\n---\n\n".join(
        f"[Source: {c['source']} — {c.get('header', '')}]\n{c['content']}"
        for c in chunks
    )

    def est_tokens(text: str) -> int:
        return len(text) // 4

    per_chunk = [
        {
            "rank": i + 1,
            "source": c["source"],
            "header": c["header"],
            "chars": len(c["content"]),
            "est_tokens": est_tokens(c["content"]),
        }
        for i, c in enumerate(chunks)
    ]

    return {
        "query": q,
        "chunks_retrieved": len(chunks),
        "total_context_chars": len(context_text),
        "total_context_est_tokens": est_tokens(context_text),
        "per_chunk": per_chunk,
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
    """Azure Bot Framework verification endpoint (GET healthcheck)."""
    return Response(status_code=200)


@app.post("/api/messages")
async def messages(request: Request):
    """Main Teams webhook — validates Azure JWT and processes messages."""
    try:
        body = await request.json()
        print(f"Received activity type: {body.get('type')}")

        activity = Activity().deserialize(body)
        auth_header = request.headers.get("Authorization", "")

        async def call_bot(turn_context: TurnContext):
            await on_message(turn_context)

        await adapter.process_activity(activity, auth_header, call_bot)
        return Response(status_code=201)

    except Exception as e:
        print(f"Teams webhook error: {type(e).__name__}: {e}")
        return Response(status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.BOT_PORT)
