import pygame
from src.pieces.piece import Piece
from src.movement_utility import generate_knight_moves

class Knight(Piece):
    images = {
        'white': pygame.image.load('gui/images/wN.svg'),
        'black': pygame.image.load('gui/images/bN.svg')
    }

    def __init__(self, color, position):
        super().__init__(color, position)
        self.set_image(Knight.images[color])
        
    def get_valid_moves(self, board):
        directions = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)
        ]
        return generate_knight_moves(self, board, directions)