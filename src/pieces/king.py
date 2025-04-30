import pygame
from src.pieces.piece import Piece

class King(Piece):
    images = {
        'white': pygame.image.load('gui/images/wK.svg'),
        'black': pygame.image.load('gui/images/bK.svg')
    }

    def __init__(self, color, position):
        super().__init__(color, position)  # Initialize the Piece class with color and position
        self.set_image(King.images[color])
        self.has_moved = False  # Track if the king has moved (important for castling)

    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position
        # Possible directions the King can move: 8 surrounding squares (horizontal, vertical, and diagonal)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),   # Top-left, Top, Top-right
            (0, -1), (0, 1),              # Left, Right
            (1, -1), (1, 0), (1, 1)       # Bottom-left, Bottom, Bottom-right
        ]
        for dx, dy in directions:
            nx, ny = row + dx, col + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                target_piece = board.get_piece_at(nx, ny)
                # If the target square is empty or contains an opponent's piece
                if target_piece is None or target_piece.color != self.color:
                    # Simulate the move
                    original_position = self.position
                    self.position = (nx, ny)
                    # Check if this move places the king in check
                    if not self.is_in_check(board):
                        valid_moves.append((nx, ny))  # Add the move if it doesn't place the king in check
                    # Revert the position back after checking
                    self.position = original_position
        return valid_moves

    def is_in_check(self, board):
        """
        This helper method checks if the king is in check by any opponent's piece.
        """
        row, col = self.position
        # Check for threats from opponent's pieces
        for r in range(8):
            for c in range(8):
                opponent_piece = board.get_piece_at(r, c)
                if opponent_piece and opponent_piece.color != self.color:
                    # Check if any piece can attack the king's position
                    if (opponent_piece.get_valid_moves(board) and (row, col) in opponent_piece.get_valid_moves(board)):
                        print('The King is in check')
                        return True  # The king is in check
                    else:
                        return False
