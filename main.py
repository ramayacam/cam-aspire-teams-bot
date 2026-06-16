from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from config.settings import settings

app = FastAPI(title="Aspire Knowledge Bot")


@app.get("/health")
async def health():
    return {"status": "ok", "message": "Bot is running"}


@app.post("/api/messages")
async def messages(request: Request):
    try:
        body = await request.json()
        return JSONResponse({
            "status": "received",
            "message": "Processing your request..."
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.get("/")
async def root():
    return {"message": "Aspire Knowledge Bot API - Teams Integration"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.BOT_PORT)
