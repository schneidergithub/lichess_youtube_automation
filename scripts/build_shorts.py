from moviepy.video.io.VideoFileClip import VideoFileClip
from pathlib import Path


def build_shorts(input_video="videos/puzzle.mp4", output="videos/puzzle_short.mp4"):

    Path("videos").mkdir(exist_ok=True)

    clip = VideoFileClip(input_video)

    # Resize for vertical format
    short = clip.resized(height=1920)

    short.write_videofile(
        output,
        codec="libx264",
        audio=False
    )

    clip.close()
    short.close()