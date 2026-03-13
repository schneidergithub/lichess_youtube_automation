
import chess
import chess.svg
import cairosvg

def render_frames(fen, moves):
    board = chess.Board(fen)
    frames = []

    svg = chess.svg.board(board)
    with open("frame_0.svg","w") as f:
        f.write(svg)
    cairosvg.svg2png(url="frame_0.svg", write_to="frame_0.png")
    frames.append("frame_0.png")

    for i, move in enumerate(moves):
        board.push(chess.Move.from_uci(move))
        svg = chess.svg.board(board)
        name = f"frame_{i+1}"
        with open(f"{name}.svg","w") as f:
            f.write(svg)
        cairosvg.svg2png(url=f"{name}.svg", write_to=f"{name}.png")
        frames.append(f"{name}.png")

    return frames
