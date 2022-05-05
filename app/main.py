from typing import Optional

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

from model import ChatBot

app = FastAPI()


@app.post("/", response_class=JSONResponse)
@app.get("/", response_class=JSONResponse)
async def root(message: Optional[str] = Form(None)):
    # if the Form is not None, then get a reply from the bot
    if message is not None:
        # gets a response of the AI bot
        return {'reply': chatbot.get_reply(message)}


# initialises the chatbot model and starts the uvicorn app
if __name__ == "__main__":
    chatbot = ChatBot()
    uvicorn.run(app, host="0.0.0.0", port=8000)
