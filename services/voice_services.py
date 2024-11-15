from decouple import config
from moviepy.editor import VideoFileClip
from openai import OpenAI # pip install -U openai

ELEVENLABS_API_KEY = config("elevenlabs_api_key")
client = OpenAI(
    base_url="https://api.avalai.ir/v1",
    api_key="aa-pAkuHIOE46mbKqVaqwXhuN2k7rf9fUXJ5CyFBR1jEAV4v80w"
)

def extract_audio(video_path, folder):
    video = VideoFileClip(str(video_path))
    audio_output_path=f"{folder}/audio_extracted.wav"
    video.audio.write_audiofile(str(audio_output_path))
    return str(audio_output_path)

def transcribe_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format="text"
        )
    return transcript