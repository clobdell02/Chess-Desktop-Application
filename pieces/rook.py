import pygame
from pieces.piece import Piece
from movement_utility import generate_sliding_moves

class Rook(Piece):
    images = {
        'white': pygame.image.load('images/wR.svg'),
        'black': pygame.image.load('images/bR.svg')
    }

    def __init__(self, color, position):
        super().__init__(color, position)
        image_path = Rook.images[color]
        self.image = pygame.image.load(image_path) # Load the image
        self.image = pygame.transform.scale(self.image, (75, 75))  # Scale the image to fit the board square (optional)

    def get_valid_moves(self, board):
        # Logic to get all valid moves for a queen (horizontal, vertical, diagonal)
        directions = [
            (1, 0), (-1, 0), # Vertical
            (0, 1), (0, -1), # Horizontal
        ]
        return generate_sliding_moves(self, board, directions)