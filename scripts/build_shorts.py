
from moviepy.editor import VideoFileClip

def build_shorts():

    clip = VideoFileClip("videos/puzzle.mp4")

    clip = clip.crop(x_center=clip.w/2, width=1080)
    clip = clip.resize(height=1920)

    clip.write_videofile("shorts/puzzle_short.mp4")
