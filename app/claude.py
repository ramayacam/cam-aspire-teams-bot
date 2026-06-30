"""
Claude client for the Aspire bot.

ask() returns a tuple: (answer_text, usage_dict)
usage_dict has real token counts from the API, or zeros on failure.
"""

import time
import anthropic

from config.settings import settings

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 1024
MAX_RETRIES = 3
RETRY_BASE_DELAY = 1.0

SYSTEM_PROMPT = """You are Aspi, the Aspire Cloud knowledge assistant for CAM Property Services, a commercial property services company in California (janitorial, landscape, maintenance, floor care, power washing).

You help staff with Aspire Cloud (https://cloud.youraspire.com/), a field service management platform.

VOICE
- Answer directly and confidently, in your own voice, as an Aspire expert would.
- Do NOT add filler like "according to the documentation," "based on the documentation," or "the documentation says." Just give the answer.
- Use the reference material provided in the user message as your source of truth, but present the answer as your own expert knowledge — not as a quote from a document.

HONESTY (this is not hedging — it is essential)
- The reference material is your only reliable source. If it does not contain the answer, say so plainly and directly: tell the user the topic isn't something you can help with yet, and point them to https://guide.youraspire.com/ or AspireCare / their system administrator.
- Never invent features, menu paths, permissions, or steps. Confidence means answering clearly what you DO know — not guessing at what you don't.
- If the user states something false about Aspire, correct it directly.

HOW TO ANSWER
- Be concise and direct. Match the length of the answer to the complexity of the question.
- For processes, use numbered steps. Mention required permissions when relevant.
- For comparisons, use a short table or clear side-by-side prose.
- Use plain language. Briefly explain any technical term you must use.
- When relevant, ground examples in CAM's business (commercial properties, fixed-payment contracts, work orders for special projects).

TONE
Professional, helpful colleague. Focus on what the user CAN do. After answering, the user should know exactly what to do next."""


EMPTY_USAGE = {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_read_tokens": 0,
    "cache_creation_tokens": 0,
}


class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    def _build_messages(self, question, context, history):
        context_text = "\n\n---\n\n".join(
            f"[Source: {c['source']} — {c.get('header', '')}]\n{c['content']}"
            for c in context
        )
        messages = []
        if history:
            messages.extend(history[-6:])
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

    def ask(self, question, context, history=None):
        """Returns (answer_text, usage_dict)."""
        if not context:
            return (
                "I don't have information about that in my knowledge base. "
                "Please check the Aspire guide at https://guide.youraspire.com/ "
                "or contact your system administrator.",
                dict(EMPTY_USAGE),
            )

        messages = self._build_messages(question, context, history or [])
        system_blocks = [{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }]

        for attempt in range(MAX_RETRIES):
            try:
                response = self.client.messages.create(
                    model=MODEL,
                    max_tokens=MAX_TOKENS,
                    system=system_blocks,
                    messages=messages,
                )
                parts = [b.text for b in response.content if hasattr(b, "text")]
                text = "".join(parts).strip()

                u = response.usage
                usage = {
                    "input_tokens": getattr(u, "input_tokens", 0) or 0,
                    "output_tokens": getattr(u, "output_tokens", 0) or 0,
                    "cache_read_tokens": getattr(u, "cache_read_input_tokens", 0) or 0,
                    "cache_creation_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
                }

                if not text:
                    text = (
                        "I wasn't able to generate an answer. Please rephrase "
                        "your question or check https://guide.youraspire.com/."
                    )
                return text, usage

            except anthropic.RateLimitError:
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_BASE_DELAY * (2 ** attempt))
                    continue
                return ("The system is busy right now. Please wait a moment and ask again.", dict(EMPTY_USAGE))

            except anthropic.APIStatusError as e:
                if 500 <= e.status_code < 600 and attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_BASE_DELAY * (2 ** attempt))
                    continue
                print(f"Anthropic APIStatusError {e.status_code}: {e}")
                return ("The Aspire assistant is temporarily unavailable. Please try again in a few minutes.", dict(EMPTY_USAGE))

            except anthropic.APIConnectionError:
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_BASE_DELAY * (2 ** attempt))
                    continue
                return ("I couldn't reach the assistant service. Please try again shortly.", dict(EMPTY_USAGE))

            except Exception as e:
                print(f"Unexpected Claude error: {type(e).__name__}: {e}")
                return ("Something went wrong on my end. Please try again.", dict(EMPTY_USAGE))

        return ("The system is busy right now. Please try again in a moment.", dict(EMPTY_USAGE))
