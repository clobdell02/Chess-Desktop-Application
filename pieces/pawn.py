from pieces.piece import Piece
from movement_utility import _is_square_empty

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)  # Call the constructor of the Piece class
        self.has_moved = False  # To track if the pawn has moved for special rules like the first move

    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position
        direction = 1 if self.color == 'white' else -1  # White moves up, black moves down

        # 1. Normal forward move (check if the square ahead is empty)
        if self._is_square_empty(row + direction, col, board):
            valid_moves.append((row + direction, col))

            # 2. First move: Check if the pawn can move two squares forward
            if not self.has_moved and self._is_square_empty(row + 2 * direction, col, board):
                valid_moves.append((row + 2 * direction, col))

        # 3. Diagonal captures: Use helper function to check diagonals for opponent's pieces
        valid_moves.extend(self._generate_pawn_capture_moves(board))

        # 5. Promotion: If the pawn reaches the final rank, add promotion moves
        valid_moves.extend(self._generate_promotion_moves())

        return valid_moves

    def _generate_pawn_capture_moves(self, board):
        """Generate possible diagonal capture moves for the pawn."""
        moves = []
        row, col = self.position
        directions = [(-1, -1), (-1, 1)] if self.color == 'black' else [(1, -1), (1, 1)]

        for dx, dy in directions:
            nx, ny = row + dx, col + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                target_piece = board.get_piece_at(nx, ny)
                if target_piece and target_piece.color != self.color:
                    moves.append((nx, ny))  # Can capture an opponent's piece
        return moves
    
    def _generate_promotion_moves(self):
        """Generate possible promotion moves when the pawn reaches the promotion rank."""
        moves = []
        row, col = self.position

        # If the pawn reaches the promotion rank (rank 8 for white, rank 1 for black)
        if (self.color == 'white' and row == 6) or (self.color == 'black' and row == 1):
            # Promotion could lead to a choice of new piece: Queen, Rook, Bishop, or Knight
            moves.append(('promote', (row + 1, col)))  # Placeholder for promotion logic
        return moves