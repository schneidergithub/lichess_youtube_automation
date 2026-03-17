
import requests

def fetch_puzzle():
    url = "https://lichess.org/api/puzzle/daily"
    #url = "https://lichess.org/api/puzzle/LQQn9"

    r = requests.get(url)
    r.raise_for_status()
    return r.json()
