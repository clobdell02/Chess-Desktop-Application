import pygame
from src.pieces.piece import Piece
from src.movement_utility import generate_sliding_moves

class Rook(Piece):
    images = {
        'white': pygame.image.load('gui/images/wR.svg'),
        'black': pygame.image.load('gui/images/bR.svg')
    }

    def __init__(self, color, position):
        super().__init__(color, position)
        self.set_image(Rook.images[color]) # using the preloaded and scaled image
        self.has_moved = False  # Track if the rook has moved (important for castling)

    def get_valid_moves(self, board):
        # Logic to get all valid moves for a queen (horizontal, vertical, diagonal)
        directions = [
            (1, 0), (-1, 0), # Vertical
            (0, 1), (0, -1), # Horizontal
        ]
        return generate_sliding_moves(self, board, directions)