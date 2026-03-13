
def generate_script(puzzle, best_move):

    theme = puzzle["puzzle"]["themes"][0]

    return f'''
Today’s chess puzzle.

Look closely at the board.

The winning move is {best_move}.

This tactic demonstrates the theme: {theme}.

Pause the video and see if you can find the move.

Subscribe for daily chess puzzles.
'''
