"""
Bot orchestration: ties retrieval (knowledge) to generation (claude).
Logs token usage for each query to stdout (visible in Render logs).

Kept intentionally thin. Heavy lifting lives in knowledge.py and claude.py.
Conversation history is in-memory (per-process). It is NOT persistent: a
Render restart clears it. For 10 sessions/day that's an acceptable tradeoff;
swap in Supabase here later if persistence is needed.
"""

from app.knowledge import KnowledgeBase
from app.claude import ClaudeClient

knowledge = KnowledgeBase()
claude = ClaudeClient()

_conversations = {}
MAX_HISTORY_MESSAGES = 10
MAX_TRACKED_USERS = 500


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


def _log_usage(user_id: str, question: str, usage: dict):
    """Print token usage to stdout — shows up in Render logs."""
    short_q = question[:80].replace("\n", " ")
    print(
        f"[USAGE] user={user_id} | "
        f"input={usage.get('input_tokens', 0)} | "
        f"output={usage.get('output_tokens', 0)} | "
        f"cache_read={usage.get('cache_read_tokens', 0)} | "
        f"cache_creation={usage.get('cache_creation_tokens', 0)} | "
        f"q='{short_q}'"
    )


async def handle_message(text: str, user_id: str = "default") -> str:
    text = (text or "").strip()
    if not text:
        return "Please ask a question about Aspire Cloud."

    if text.lower() in {"hi", "hello", "hey", "hola", "buenas"}:
        return (
            "Hi! I'm the Aspire Cloud assistant for CAM. Ask me about work "
            "tickets, scheduling, invoicing, opportunities, and more."
        )

    try:
        context = knowledge.search(text, top_k=6)
        history = _get_history(user_id)
        answer, usage = claude.ask(text, context, history)

        _log_usage(user_id, text, usage)
        _save_turn(user_id, text, answer)
        return answer
    except Exception as e:
        print(f"handle_message error: {type(e).__name__}: {e}")
        return "Something went wrong. Please try again."
