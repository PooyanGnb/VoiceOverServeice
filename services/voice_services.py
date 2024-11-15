from decouple import config
from moviepy.editor import VideoFileClip
from openai import OpenAI 
from langchain_openai import OpenAI as Translate

ELEVENLABS_API_KEY = config("elevenlabs_api_key")
base_url="https://api.avalai.ir/v1"
api_key="aa-pAkuHIOE46mbKqVaqwXhuN2k7rf9fUXJ5CyFBR1jEAV4v80w"
client = OpenAI(
    base_url=base_url,
    api_key=api_key
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

def translate_text(text, target_language):
    translation = Translate(
        model="gpt-3.5-turbo-instruct",
        base_url=base_url,
        api_key=api_key
    )
    result = translation.invoke(f"Translate the following Persian text to {target_language}:\n\n{text}")
    return result