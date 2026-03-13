
from moviepy.editor import ImageSequenceClip, AudioFileClip

def build_video(frames):
    clip = ImageSequenceClip(frames, fps=1)
    audio = AudioFileClip("audio.mp3")
    final = clip.set_audio(audio)
    final.write_videofile("videos/puzzle.mp4", codec="libx264")
