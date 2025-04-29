# pieces/piece.py
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position  # position as a tuple (row, col)

    def get_valid_moves(self, board):
        raise NotImplementedError("This method should be overridden by subclasses.")
