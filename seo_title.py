
def generate_title(puzzle):
    rating = puzzle["puzzle"]["rating"]
    theme = puzzle["puzzle"]["themes"][0]

    return f"Can You Solve This {rating}-Rated Chess Puzzle? ({theme.capitalize()})"
