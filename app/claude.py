"""
Claude client for the Aspire bot.

Responsibilities:
  * Build the prompt from retrieved context chunks + conversation history.
  * Call the Anthropic API with retry/backoff on transient errors.
  * Return clean text, or a user-friendly message on failure.

Design notes:
  * The static system prompt is marked for prompt caching so repeated calls
    are cheaper. The dynamic context (retrieved chunks) is NOT cached because
    it changes every question.
  * Model and limits are module constants so they're easy to tune.
"""

import time
import anthropic

from config.settings import settings

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 1024
MAX_RETRIES = 3
RETRY_BASE_DELAY = 1.0  # seconds, doubles each attempt

SYSTEM_PROMPT = """You are the Aspire Cloud Knowledge Agent for CAM Property Services, a commercial property services company in California (janitorial, landscape, maintenance, floor care, power washing).

You answer questions about Aspire Cloud (https://cloud.youraspire.com/), a field service management platform.

HOW TO ANSWER
- Answer ONLY from the documentation provided in the user message. Do not invent features, menu paths, or permissions.
- If the provided documentation does not contain the answer, say so plainly and point the user to https://guide.youraspire.com/ or their system administrator. Do not guess.
- Be concise and direct. Match the length of the answer to the complexity of the question.
- For processes, use numbered steps. Mention required permissions when the documentation lists them.
- For comparisons, use a short table or clear side-by-side prose.
- Use plain language. Briefly explain any technical term you must use.
- When relevant, ground examples in CAM's business (commercial properties, fixed-payment contracts, work orders for special projects).

TONE
Professional, helpful colleague. Focus on what the user CAN do. After answering, the user should know exactly what to do next."""


class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    def _build_messages(self, question: str, context: list, history: list):
        context_text = "\n\n---\n\n".join(
            f"[Source: {c['source']} — {c.get('header', '')}]\n{c['content']}"
            for c in context
        )

        messages = []
        if history:
            messages.extend(history[-6:])  # last 3 exchanges

        messages.append({
            "role": "user",
            "content": (
                "Answer the question using ONLY the documentation below.\n\n"
                "=== DOCUMENTATION ===\n"
                f"{context_text}\n"
                "=== END DOCUMENTATION ===\n\n"
                f"Question: {question}"
            ),
        })
        return messages

    def ask(self, question: str, context: list, history: list = None) -> str:
        """Return Claude's answer text, or a friendly error string."""
        if not context:
            return (
                "I don't have information about that in my knowledge base. "
                "Please check the Aspire guide at https://guide.youraspire.com/ "
                "or contact your system administrator."
            )

        messages = self._build_messages(question, context, history or [])

        system_blocks = [{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }]

        last_error = None
        for attempt in range(MAX_RETRIES):
            try:
                response = self.client.messages.create(
                    model=MODEL,
                    max_tokens=MAX_TOKENS,
                    system=system_blocks,
                    messages=messages,
                )
                # Concatenate all text blocks (defensive vs multi-block output)
                parts = [b.text for b in response.content if hasattr(b, "text")]
                text = "".join(parts).strip()
                return text or (
                    "I wasn't able to generate an answer. Please rephrase your "
                    "question or check https://guide.youraspire.com/."
                )

            except anthropic.RateLimitError as e:
                last_error = e
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_BASE_DELAY * (2 ** attempt))
                    continue
                return (
                    "The system is busy right now. Please wait a moment and "
                    "ask again."
                )

            except anthropic.APIStatusError as e:
                last_error = e
                # 5xx are transient; retry. 4xx are not; fail fast.
                if 500 <= e.status_code < 600 and attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_BASE_DELAY * (2 ** attempt))
                    continue
                print(f"Anthropic APIStatusError {e.status_code}: {e}")
                return (
                    "The Aspire assistant is temporarily unavailable. Please "
                    "try again in a few minutes."
                )

            except anthropic.APIConnectionError as e:
                last_error = e
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_BASE_DELAY * (2 ** attempt))
                    continue
                return (
                    "I couldn't reach the assistant service. Please try again "
                    "shortly."
                )

            except Exception as e:  # noqa: BLE001 — last-resort safety net
                print(f"Unexpected Claude error: {type(e).__name__}: {e}")
                return "Something went wrong on my end. Please try again."

        print(f"All retries exhausted: {last_error}")
        return "The system is busy right now. Please try again in a moment."
