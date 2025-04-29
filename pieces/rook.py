from pieces.piece import Piece
from movement_utility import generate_sliding_moves

class Rook(Piece):
    def get_valid_moves(self, board):
        # Logic to get all valid moves for a queen (horizontal, vertical, diagonal)
        directions = [
            (1, 0), (-1, 0), # Vertical
            (0, 1), (0, -1), # Horizontal
        ]
        return generate_sliding_moves(self, board, directions)