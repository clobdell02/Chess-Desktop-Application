# pieces/piece.py
class Piece:
    def __init__(self, color, position):
        self.color = color  # The color of the piece (white or black)
        self.position = position  # The position on the board (row, col)
        self.image = None  # Image will be handled by the subclass
        self.has_moved = False  # Keep track of whether the piece has moved

    def get_valid_moves(self, board):
        raise NotImplementedError("This method should be overridden by subclasses.")
