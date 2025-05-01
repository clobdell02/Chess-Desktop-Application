import pygame
from src.pieces.piece import Piece
from src.movement_utility import is_square_empty

class Pawn(Piece):
    images = {
        'white': pygame.image.load('gui/images/wP.svg'),
        'black': pygame.image.load('gui/images/bP.svg')
    }

    def __init__(self, color, position):
        super().__init__(color, position)  # Call the constructor of the Piece class
        self.set_image(Pawn.images[color])
        self.has_moved = False  # To track if the pawn has moved for special rules like the first move

    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position
        direction = -1 if self.color == 'white' else 1  # White moves up, black moves down
        # 1. Normal forward move (check if the square ahead is empty)
        if is_square_empty(row + direction, col, board):
            valid_moves.append((row + direction, col))
            # 2. First move: Check if the pawn can move two squares forward
            if not self.has_moved and is_square_empty(row + 2 * direction, col, board):
                valid_moves.append((row + 2 * direction, col))
        # 3. Diagonal captures: Use helper function to check diagonals for opponent's pieces
        valid_moves.extend(self.generate_pawn_capture_moves(board))
        # 4. Promotion: If the pawn reaches the final rank, add promotion moves
        valid_moves.extend(self.generate_promotion_moves(board))
        return valid_moves

    def generate_pawn_capture_moves(self, board):
        """Generate possible diagonal capture moves for the pawn."""
        moves = []
        row, col = self.position
        if self.color == 'black':
            directions = [(1, -1), (1, 1)]
        else:
            directions = [(-1, -1), (-1, 1)]
        for dx, dy in directions:
            nx, ny = row + dx, col + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                target_piece = board.get_piece_at(nx, ny)
                if target_piece and target_piece.color != self.color:
                    moves.append((nx, ny))  # Can capture an opponent's piece
        return moves
    
    def generate_promotion_moves(self, board):
        """Generate possible promotion moves when the pawn reaches the promotion rank."""
        moves = []
        row, col = self.position
        if self.color == 'white':
            direction = -1
        elif self.color == 'black':
            direction = 1
        target_row = row + direction
        # is target in the range of the board
        if not (0 <= target_row < 8):
            return moves
        # check standard forward moves
        if is_square_empty(target_row, col, board):
            if (self.color == 'white' and target_row == 0) or (self.color == 'black' and target_row == 7):
                moves.append(('promotion', (target_row, col)))
        # check diagnoal captures for promotion
        for target in self.generate_pawn_capture_moves(board):
            if (self.color == 'white' and target_row == 0) or (self.color == 'black' and target_row == 7):
                moves.append(('promotion', target))
        return moves