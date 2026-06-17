import anthropic
from config.settings import settings

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 2048

SYSTEM_PROMPT = """You are an expert assistant for Aspire Cloud (https://cloud.youraspire.com/).
You work for CAM Property Services.

RULES:
- Use plain, understandable language
- Short and direct responses
- Numbered steps for processes
- Mention required permissions when relevant
- If you don't know: say so and direct to https://guide.youraspire.com/
- Keep responses as short as the question allows
- Comparisons: use tables
- 2-3 items: prose | 4+ items: bullets
"""


class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    def ask(self, question: str, context: list, history: list = None) -> str:
        context_text = "\n\n---\n\n".join([
            f"Source: {c['source']}\n{c['content']}" for c in context
        ])

        messages = []

        if history:
            messages.extend(history[-6:])

        messages.append({
            "role": "user",
            "content": (
                f"Use ONLY the following documentation to answer.\n\n"
                f"Documentation:\n{context_text}\n\n"
                f"Question: {question}"
            )
        })

        response = self.client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=messages,
        )

        return response.content[0].text
