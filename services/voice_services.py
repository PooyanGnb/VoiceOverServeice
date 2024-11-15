from decouple import config
from moviepy.editor import VideoFileClip

ELEVENLABS_API_KEY = config("elevenlabs_api_key")

def extract_audio(video_path, folder):
    video = VideoFileClip(str(video_path))
    audio_output_path=f"{folder}/audio_extracted.wav"
    video.audio.write_audiofile(str(audio_output_path))
    return audio_output_path