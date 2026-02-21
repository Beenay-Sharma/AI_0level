from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# groq client
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Answer clearly and concisely."
    }
]

# request model
class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"status": "AI backend is running 🚀"}


@app.post("/chat")
async def chat(request: ChatRequest):
    # add user message to history
    messages.append({
        "role": "user",
        "content": request.message
    })

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        reply = response.choices[0].message.content

        # add assistant reply to history
        messages.append({
            "role": "assistant",
            "content": reply
        })

        return {"reply": reply}

    except Exception as e:
        return {"error": str(e)}
