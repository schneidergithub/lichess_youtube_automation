
from stockfish import Stockfish

stockfish = Stockfish("/usr/local/bin/stockfish")

def best_move(fen):
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()
