from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import glob
from pathlib import Path

def build_video(frame_dir="frames", output="videos/puzzle.mp4"):
    Path("videos").mkdir(exist_ok=True)

    frames = sorted(glob.glob(f"{frame_dir}/*.png"))
    clip = ImageSequenceClip(frames, fps=1)

    clip.write_videofile(output, codec="libx264", audio=False)
