import pygame
from pieces.piece import Piece
from movement_utility import generate_sliding_moves

class Bishop(Piece):
    images = {
        'white': pygame.image.load('images/wB.svg'),
        'black': pygame.image.load('images/bB.svg')
    }

    def __init__(self, color, position):
        super().__init__(color, position)
        self.set_image(Bishop.images[color])
        
    def get_valid_moves(self, board):
        directions = [
            (1, 1), (-1, -1), # Diagonal
            (1, -1), (-1, 1) # Anti-diagonal
        ]
        return generate_sliding_moves(self, board, directions)