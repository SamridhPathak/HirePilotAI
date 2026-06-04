from fastapi import FastAPI
from app.routes import resume, interview
from fastapi.middleware.cors import CORSMiddleware
from chatbot.chatbot_routes import router as chatbot_router
from app.routes import leaderboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)
app.include_router(interview.router)
app.include_router(chatbot_router)
app.include_router(leaderboard.router)

@app.get("/")
def home():
    return {"message": "AI Interview Backend Running 🚀"}
