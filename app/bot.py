"""
Bot orchestration: ties retrieval (knowledge) to generation (claude).

Kept intentionally thin. Heavy lifting lives in knowledge.py and claude.py.
Conversation history is in-memory (per-process). It is NOT persistent: a
Render restart clears it. For 10 sessions/day that's an acceptable tradeoff;
swap in Supabase here later if persistence is needed.
"""

from app.knowledge import KnowledgeBase
from app.claude import ClaudeClient

# Built once at import time. Loading + indexing the KB is fast (<1s).
knowledge = KnowledgeBase()
claude = ClaudeClient()

# user_id -> list of {role, content}. Bounded to avoid unbounded growth.
_conversations = {}
MAX_HISTORY_MESSAGES = 10          # 5 exchanges
MAX_TRACKED_USERS = 500            # simple safety cap on memory


def _get_history(user_id: str) -> list:
    return _conversations.get(user_id, [])


def _save_turn(user_id: str, question: str, answer: str):
    history = _conversations.get(user_id, [])
    history.append({"role": "user", "content": question})
    history.append({"role": "assistant", "content": answer})
    _conversations[user_id] = history[-MAX_HISTORY_MESSAGES:]

    # Crude eviction if too many users tracked (keeps memory bounded)
    if len(_conversations) > MAX_TRACKED_USERS:
        # Drop an arbitrary oldest-inserted key
        oldest = next(iter(_conversations))
        _conversations.pop(oldest, None)


async def handle_message(text: str, user_id: str = "default") -> str:
    """Process one user message and return the bot's reply text.
    Never raises — always returns a string suitable to show the user."""
    text = (text or "").strip()
    if not text:
        return "Please ask a question about Aspire Cloud."

    # Trivial greetings shouldn't trigger a doc search
    if text.lower() in {"hi", "hello", "hey", "hola", "buenas"}:
        return (
            "Hi! I'm the Aspire Cloud assistant for CAM. Ask me about work "
            "tickets, scheduling, invoicing, opportunities, and more."
        )

    try:
        context = knowledge.search(text, top_k=6)
        history = _get_history(user_id)
        answer = claude.ask(text, context, history)
        _save_turn(user_id, text, answer)
        return answer
    except Exception as e:  # noqa: BLE001 — must never crash the webhook
        print(f"handle_message error: {type(e).__name__}: {e}")
        return "Something went wrong. Please try again."
