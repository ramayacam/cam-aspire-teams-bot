from app.knowledge import KnowledgeBase
from app.claude import ClaudeClient

knowledge = KnowledgeBase()
claude = ClaudeClient()

# Simple in-memory conversation history per user
conversations = {}


async def handle_message(text: str, user_id: str = "default") -> str:
    try:
        # Search relevant documentation
        context = knowledge.search(text, top_k=5)

        if not context:
            return (
                "I don't have information about that in my knowledge base. "
                "Try checking https://guide.youraspire.com/"
            )

        # Get conversation history for this user
        history = conversations.get(user_id, [])

        # Ask Claude with context
        response = claude.ask(text, context, history)

        # Save to history
        history.append({"role": "user", "content": text})
        history.append({"role": "assistant", "content": response})

        # Keep only last 10 messages
        conversations[user_id] = history[-10:]

        return response

    except Exception as e:
        print(f"Error in handle_message: {str(e)}")
        return "Something went wrong. Please try again."
