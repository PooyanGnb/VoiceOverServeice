from fastapi import FastAPI

# Import routers from different modules
from routers.voice import router as voice_router

app = FastAPI()

# Include routers in the application
app.include_router(voice_router)