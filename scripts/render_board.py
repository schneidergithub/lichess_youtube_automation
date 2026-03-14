import re
import shutil
from io import StringIO
from pathlib import Path

import cairosvg
import chess
import chess.pgn
import chess.svg


BOARD_SIZE = 720
INITIAL_HOLD_FRAMES = 60
MOVE_HOLD_FRAMES = 2


def _load_start_board(puzzle):
    """
    Reconstruct the puzzle start position from PGN.

    Lichess puzzle data can be interpreted one ply differently depending on how
    `initialPly` lines up with the PGN text. To make this robust, try the
    natural interpretation first, then validate against the first solution move.
    If that fails, try one ply later.
    """
    game = chess.pgn.read_game(StringIO(puzzle["pgn"]))
    if game is None:
        raise ValueError("Unable to parse PGN from puzzle data.")

    all_moves = list(game.mainline_moves())
    first_solution = chess.Move.from_uci(puzzle["solution"][0])

    candidates = []

    # Primary interpretation
    candidates.append(puzzle["initial_ply"])

    # Common off-by-one correction
    candidates.append(puzzle["initial_ply"] + 1)

    # De-duplicate while preserving order
    seen = set()
    unique_candidates = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            unique_candidates.append(c)

    for ply_count in unique_candidates:
        if ply_count < 0 or ply_count > len(all_moves):
            continue

        board = game.board()
        for i in range(ply_count):
            board.push(all_moves[i])

        if first_solution in board.legal_moves:
            return board

    # Build a helpful error message for debugging
    debug_positions = []
    for ply_count in unique_candidates:
        if 0 <= ply_count <= len(all_moves):
            board = game.board()
            for i in range(ply_count):
                board.push(all_moves[i])
            debug_positions.append(
                (
                    f"ply_count={ply_count}, "
                    f"turn={'white' if board.turn else 'black'}, "
                    f"fen={board.fen()}"
                )
            )

    raise ValueError(
        "Could not align puzzle start position with first solution move "
        f"{puzzle['solution'][0]!r}. Tried:\n" + "\n".join(debug_positions)
    )


def render_frames(puzzle, output_dir="frames", fps=1):
    """
    Render frames for a Lichess puzzle.

    - 60-second countdown before showing the solution
    - Semi-transparent piece at original square after each move
    """
    output_path = Path(output_dir)

    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    board = _load_start_board(puzzle)
    orientation = board.turn
    frame_index = 0
    initial_hold_frames = 60 * fps

    def save_svg(svg_text, repeat=1):
        nonlocal frame_index
        for _ in range(repeat):
            filename = output_path / f"frame_{frame_index:03d}.png"
            cairosvg.svg2png(
                bytestring=svg_text.encode("utf-8"),
                write_to=str(filename),
            )
            frame_index += 1

    # Initial puzzle position with countdown overlay
    initial_svg = chess.svg.board(
        board,
        orientation=orientation,
        size=BOARD_SIZE,
        coordinates=True,
    )
    for i in range(initial_hold_frames):
        countdown = 60 - (i // fps)
        countdown_svg = (
            f'<text x="{BOARD_SIZE // 2}" y="{BOARD_SIZE // 2}" '
            'font-size="30" fill="blue" text-anchor="middle" '
            'dominant-baseline="middle" opacity="0.4">'
            f"{countdown}</text>"
        )
        svg_with_countdown = re.sub(r"(</svg>)", countdown_svg + r"\1", initial_svg)
        save_svg(svg_with_countdown)

    # Render each solution move on the resulting board
    for move_uci in puzzle["solution"]:
        move = chess.Move.from_uci(move_uci)

        if move not in board.legal_moves:
            raise ValueError(
                f"Illegal solution move {move_uci} for current position: {board.fen()}"
            )

        piece = board.piece_at(move.from_square)
        from_square = move.from_square
        board.push(move)

        move_svg = chess.svg.board(
            board,
            orientation=orientation,
            size=BOARD_SIZE,
            coordinates=True,
            arrows=[chess.svg.Arrow(move.from_square, move.to_square)],
        )

        # Overlay semi-transparent piece at original square
        if piece:
            square_name = chess.square_name(from_square)
            file = ord(square_name[0]) - ord("a")
            rank = int(square_name[1]) - 1
            x = file * BOARD_SIZE // 8
            y = (7 - rank) * BOARD_SIZE // 8 if orientation else rank * BOARD_SIZE // 8

            piece_id = f"{'w' if piece.color else 'b'}{piece.symbol().lower()}"
            piece_svg = (
                '<g opacity="0.4">'
                f'<use href="#{piece_id}" x="{x}" y="{y}" '
                f'width="{BOARD_SIZE // 8}" height="{BOARD_SIZE // 8}"/>'
                "</g>"
            )
            move_svg = re.sub(r"(</svg>)", piece_svg + r"\1", move_svg)

        save_svg(move_svg, repeat=MOVE_HOLD_FRAMES)

    return frame_index
