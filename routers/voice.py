from fastapi import APIRouter, File, UploadFile, Form, BackgroundTasks
from services.video_services import *
from services.voice_services import *


router = APIRouter(tags=["voice over"])


@router.post("/voice-over")
async def voice_over(background_tasks: BackgroundTasks, file: UploadFile = File(...), language: str = Form(...)):
    
    # Generate unique path
    working_dir = generate_unique_path()

    # Save uploaded video in this directory
    video_path = working_dir / file.filename
    with open(video_path, "wb") as buffer:
        buffer.write(await file.read())

    # Add cleanup task
    # background_tasks.add_task(cleanup_directory, working_dir)

    # extract the audio from the video
    extract_audio(video_path, working_dir)

    # return True