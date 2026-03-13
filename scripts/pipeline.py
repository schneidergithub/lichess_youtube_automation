
from fetch_puzzles import fetch_puzzle
from puzzle_filter import filter_puzzle
from stockfish_analyze import best_move
from render_board_sequence import render_frames
from generate_script import generate_script
from generate_voice import generate_voice
from build_video import build_video
from build_shorts import build_shorts
from generate_thumbnail import generate_thumbnail
from seo_title import generate_title

def main():

    puzzle = fetch_puzzle()

    if not filter_puzzle(puzzle):
        print("Puzzle filtered")
        return

    fen = puzzle["game"]["fen"]
    moves = puzzle["puzzle"]["solution"]

    move = best_move(fen)

    frames = render_frames(fen, moves)

    script = generate_script(puzzle, move)

    generate_voice(script)

    build_video(frames)

    build_shorts()

    generate_thumbnail(frames[0])

    title = generate_title(puzzle)

    print("Generated video:", title)


if __name__ == "__main__":
    main()
