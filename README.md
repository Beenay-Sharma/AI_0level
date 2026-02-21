# AI Chatbot 🤖

A full-stack AI chatbot built with FastAPI backend and vanilla HTML/CSS/JS frontend, powered by Groq's lightning-fast inference API running Llama 3.3 70b versatile.

## Features
- Real-time AI conversation
- Conversation history (remembers context)
- Clean modern chat UI
- Fast responses via Groq API

## Tech Stack
- **Backend** — Python, FastAPI
- **Frontend** — HTML, CSS, JavaScript
- **AI Model** — Llama 3.3 70B via Groq API

## Requirements
- Python 3.10+
- Groq API key (free at console.groq.com)

## Setup & Installation

1. Clone the repository
   git clone https://github.com/Beenay-Sharma/ai-chatbot.git
   cd ai-chatbot

2. Create virtual environment
   python -m venv myenv
   source myenv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Create .env file
   GROQ_API_KEY=your_groq_api_key_here

5. Run the backend
   uvicorn main:app --reload

6. Open index.html in your browser and start chatting!

## Project Structure
ai-chatbot/
├── main.py          # FastAPI backend + Groq integration
├── index.html       # Frontend chatbot UI
├── requirements.txt # Python dependencies
├── .env             # Secret keys (never push this)
└── .gitignore       # Files to ignore in git

## Simply, a mini thing at starting phase where i learned about how to use ai api's in telegram chatbots,websites and other places. With Ai,Many more things can be done .Thankyou..