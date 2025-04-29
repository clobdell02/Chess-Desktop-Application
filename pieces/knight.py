from pieces.piece import Piece
from movement_utility import generate_knight_moves

class Knight(Piece):
    def get_valid_moves(self, board):
        knight_moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)
        ]
        return generate_knight_moves(self, board, directions)