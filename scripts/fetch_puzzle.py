import requests

API = "https://lichess.org/api/puzzle/daily"

def fetch_puzzle():
    r = requests.get(API)
    r.raise_for_status()
    data = r.json()

    puzzle = data["puzzle"]
    game = data["game"]

    return {
        "id": puzzle["id"],
        "rating": puzzle["rating"],
        "themes": puzzle["themes"],
        "solution": puzzle["solution"],
        "initial_ply": puzzle["initialPly"],
        "pgn": game["pgn"]
    }
