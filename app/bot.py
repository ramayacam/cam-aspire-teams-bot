"""
Bot orchestration: ties retrieval (knowledge) to generation (claude).

Relevance gate: off-topic questions (pure BM25 ~0) get a scope reply WITHOUT
calling Claude. Token usage is logged to stdout (visible in Render logs).
"""

from app.knowledge import KnowledgeBase
from app.claude import ClaudeClient

knowledge = KnowledgeBase()
claude = ClaudeClient()

_conversations = {}
MAX_HISTORY_MESSAGES = 10
MAX_TRACKED_USERS = 500

RELEVANCE_FLOOR = 1.0

OFF_TOPIC_REPLY = (
    "I'm the Aspire Cloud assistant for CAM — I can only help with questions "
    "about Aspire Cloud (work tickets, scheduling, invoicing, opportunities, "
    "and related topics). Try asking me something about those areas."
)


def _get_history(user_id: str) -> list:
    return _conversations.get(user_id, [])


def _save_turn(user_id: str, question: str, answer: str):
    history = _conversations.get(user_id, [])
    history.append({"role": "user", "content": question})
    history.append({"role": "assistant", "content": answer})
    _conversations[user_id] = history[-MAX_HISTORY_MESSAGES:]
    if len(_conversations) > MAX_TRACKED_USERS:
        oldest = next(iter(_conversations))
        _conversations.pop(oldest, None)


def _log_usage(user_id, question, usage, chunks, gated=False):
    short_q = question[:80].replace("\n", " ")
    if gated:
        print(f"[USAGE] user={user_id} | GATED (off-topic, no Claude call) | q='{short_q}'")
        return
    print(
        f"[USAGE] user={user_id} | "
        f"chunks={chunks} | "
        f"input={usage.get('input_tokens', 0)} | "
        f"output={usage.get('output_tokens', 0)} | "
        f"cache_read={usage.get('cache_read_tokens', 0)} | "
        f"cache_creation={usage.get('cache_creation_tokens', 0)} | "
        f"q='{short_q}'"
    )


async def handle_message(text: str, user_id: str = "default") -> str:
    """Process one user message and return the bot's reply text.
    Never raises — always returns a string suitable to show the user."""
    text = (text or "").strip()
    if not text:
        return "Please ask a question about Aspire Cloud."

    if text.lower() in {"hi", "hello", "hey", "hola", "buenas"}:
        return (
            "Hi! I'm Aspi 🤖, the Aspire Cloud assistant for CAM. Ask me about "
            "work tickets, scheduling, invoicing, opportunities, and more."
        )

    try:
        result = knowledge.search_scored(text, top_k=6)
        chunks = result["chunks"]

        # Relevance gate: off-topic questions never reach Claude.
        if result["max_pure_bm25"] <= RELEVANCE_FLOOR or not chunks:
            _log_usage(user_id, text, {}, 0, gated=True)
            _save_turn(user_id, text, OFF_TOPIC_REPLY)
            return OFF_TOPIC_REPLY

        history = _get_history(user_id)
        answer, usage = claude.ask(text, chunks, history)   # ✅ desempaca la tupla

        _log_usage(user_id, text, usage, len(chunks))
        _save_turn(user_id, text, answer)
        return answer
    except Exception as e:  # noqa: BLE001
        print(f"handle_message error: {type(e).__name__}: {e}")
        return "Something went wrong. Please try again."
