# pieces/piece.py
import pygame

class Piece:
    def __init__(self, color, position):
        self.color = color  # The color of the piece (white or black)
        self.position = position  # The position on the board (row, col)
        self.image = None  # Image will be handled by the subclass

    def set_image(self, image):
        # used to crop and scale piece images
        cropped = self.crop_surface(image)
        self.image = pygame.transform.smoothscale(cropped, (50, 50))

    def crop_surface(self, image):
        boundary = image.get_bounding_rect()
        return image.subsurface(boundary).copy()

    def get_valid_moves(self, board):
        raise NotImplementedError("This method should be overridden by subclasses.")
