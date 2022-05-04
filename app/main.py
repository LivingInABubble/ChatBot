from typing import Optional

import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from model import ChatBot

app = FastAPI()

# mounts the static folder that contains the css file
app.mount("/static", StaticFiles(directory="static"), name="static")

# locates the template files that will be modified at run time
# with the dialog form the user and bot
templates = Jinja2Templates(directory="templates")


@app.post("/", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def root(request: Request, message: Optional[str] = Form(None)):
    # if the Form is not None, then get a reply from the bot
    if message is not None:
        # gets a response of the AI bot
        return chatbot.get_reply(message)


# initialises the chatbot model and starts the uvicorn app
if __name__ == "__main__":
    chatbot = ChatBot()
    uvicorn.run(app, host="0.0.0.0", port=8000)
