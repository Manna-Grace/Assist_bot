import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pydantic import BaseModel

# Import your database and agent files
from database import engine
from app.models import Base
from agent_bot import agent

# 1. Start the Database
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up: Initializing database tables...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    print("Shutting down: Disposing database engine...")
    await engine.dispose()

app = FastAPI(title="Whiff n Whisk API", lifespan=lifespan)

# 2. CORS Security Bypass (Crucial for React!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows your React app to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Define what the incoming message looks like
class ChatRequest(BaseModel):
    message: str

# 4. The actual Web Endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Pass the message to your AI agent
        result = await agent.run(request.message)
        return {"reply": result.output}
    except Exception as e:
        # If something crashes inside the AI, send the error back to React
        return {"reply": f"Backend Error: {str(e)}"}

@app.get("/")
def health_check():
    return {"status": "Whiff n Whisk Backend is online!"}