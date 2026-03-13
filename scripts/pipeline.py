from fetch_puzzle import fetch_puzzle
from render_board import render_frames
from build_video import build_video
from build_shorts import build_shorts

def run():
    puzzle = fetch_puzzle()

    print("Puzzle:", puzzle["id"])
    print("Rating:", puzzle["rating"])
    print("Themes:", puzzle["themes"])

    render_frames(puzzle)
    build_video()
    build_shorts()

    print("Video created.")

if __name__ == "__main__":
    run()
