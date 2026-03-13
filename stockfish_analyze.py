
from stockfish import Stockfish

stockfish = Stockfish("engine/stockfish")

def best_move(fen):
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()
