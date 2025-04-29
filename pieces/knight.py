import pygame
from pieces.piece import Piece
from movement_utility import generate_knight_moves

class Knight(Piece):
    images = {
        'white': pygame.image.load('images/wN.svg'),
        'black': pygame.image.load('images/bN.svg')
    }

    def __init__(self, color, position):
        super().__init__(color, position)
        image_path = Knight.images[color]
        self.image = pygame.image.load(image_path) # Load the image
        self.image = pygame.transform.scale(self.image, (75, 75))  # Scale the image to fit the board square (optional)
        
    def get_valid_moves(self, board):
        knight_moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)
        ]
        return generate_knight_moves(self, board, directions)