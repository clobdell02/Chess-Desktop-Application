from pieces.piece import Piece
from movement_utility import generate_sliding_moves

class Bishop(Piece):
    def get_valid_moves(self, board):
        # Logic to get all valid moves for a queen (horizontal, vertical, diagonal)
        directions = [
            (1, 1), (-1, -1), # Diagonal
            (1, -1), (-1, 1) # Anti-diagonal
        ]
        return generate_sliding_moves(self, board, directions)