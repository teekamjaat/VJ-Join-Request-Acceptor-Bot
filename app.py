# app.py

import threading
import uvicorn
from fastapi import FastAPI
from bot import run_bot  # This is the function you just added in bot.py

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

def start_http_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")

if __name__ == "__main__":
    # Start FastAPI server in the background
    threading.Thread(target=start_http_server, daemon=True).start()

    # Start the Telegram bot
    run_bot()
