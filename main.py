import re
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes
from botframework.connector.auth import MicrosoftAppCredentials
from app.bot import handle_message
from app.knowledge import KnowledgeBase
from config.settings import settings

app = FastAPI(title="Aspire Knowledge Bot")

kb = KnowledgeBase()

# Bot Framework adapter — configured for a Single Tenant Azure Bot.
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


WELCOME_MESSAGE = (
    "👋 Hi! I'm Aspi 🤖, the Aspire Cloud knowledge assistant for CAM.\n\n"
    "Ask me anything about Aspire Cloud and I'll answer based on our internal "
    "documentation. For example:\n\n"
    "• How do I complete a work ticket?\n"
    "• What's the difference between a contract and a work order?\n"
    "• How do I create a change order?\n"
    "• What is Fixed Payment vs T&M?\n\n"
    "I cover modules like Work Tickets, Scheduling, Invoicing, Opportunities, "
    "Properties, and more. For topics outside our documentation, I'll point you "
    "to the official guide at guide.youraspire.com.\n\n"
    "Just type your question to get started."
)


async def on_turn(turn_context: TurnContext):
    """Routes incoming activities by type."""
    activity = turn_context.activity

    # New member added → send welcome ONCE (only if it's not the bot itself)
    if activity.type == ActivityTypes.conversation_update:
        if activity.members_added:
            bot_id = activity.recipient.id if activity.recipient else None
            for member in activity.members_added:
                if member.id != bot_id:
                    await turn_context.send_activity(WELCOME_MESSAGE)
                    break
        return

    # Only handle text messages
    if activity.type != ActivityTypes.message:
        return

    text = activity.text or ""
    text = re.sub(r"<at>.*?</at>\s*", "", text).strip()
    if not text:
        return

    # Show "typing..." indicator while we think (no token cost)
    await turn_context.send_activity(Activity(type=ActivityTypes.typing))

    user_id = activity.from_property.id if activity.from_property else "unknown"
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


@app.get("/debug/tokens")
async def debug_tokens(q: str = "How do I complete a work ticket?"):
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
    try:
        body = await request.json()
        question = body.get("question", "")
        if not question:
            return JSONResponse({"error": "No question provided"})
        answer = await
