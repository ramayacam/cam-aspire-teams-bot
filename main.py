from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.bot import handle_message
from config.settings import settings

app = FastAPI(title="Aspire Knowledge Bot")


@app.get("/health")
async def health():
    return {"status": "ok", "message": "Bot is running"}


@app.get("/")
async def root():
    return {"message": "Aspire Knowledge Bot API"}


@app.post("/ask")
async def ask(request: Request):
    """Test endpoint - send a question and get a response"""
    try:
        body = await request.json()
        question = body.get("question", "")

        if not question:
            return JSONResponse({"error": "No question provided"})

        response = await handle_message(question)

        return JSONResponse({
            "question": question,
            "answer": response
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.post("/api/messages")
async def messages(request: Request):
    """Teams webhook - will be completed in Teams integration step"""
    try:
        body = await request.json()
        text = body.get("text", "")

        if not text:
            return JSONResponse({"error": "No message text"})

        response = await handle_message(text)

        return JSONResponse({
            "type": "message",
            "text": response
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.BOT_PORT)
