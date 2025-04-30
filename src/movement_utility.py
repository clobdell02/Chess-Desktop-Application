from src.pieces import piece

def generate_sliding_moves(piece, board, directions):
    """
    Helper function to generate sliding moves (used by Rook, Bishop, Queen).
    `directions` is a list of (dx, dy) tuples representing movement directions.
    """
    moves = []
    x, y = piece.position
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8:
            target = board.get_piece_at(nx, ny)
            if target is None:
                moves.append((nx, ny))  # Empty space
            elif target.color != piece.color:
                moves.append((nx, ny))  # Can capture opponent piece
                break  # Can't jump over pieces
            else:
                break  # Own piece blocks path
            nx += dx
            ny += dy
    return moves

def generate_knight_moves(piece, board, directions):
    """Helper function to generate knight moves."""   
    valid_moves = []
    x, y = piece.position
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            target = board.get_piece_at(nx, ny)
            if target is None or target.color != piece.color:
                valid_moves.append((nx, ny))
    return valid_moves

def is_square_empty(row, col, board):
        """Helper function to check if the given square is empty."""
        if 0 <= row < 8 and 0 <= col < 8:
            return board.get_piece_at(row, col) is None
        return False