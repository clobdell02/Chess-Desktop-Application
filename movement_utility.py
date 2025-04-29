# movement_utils.py

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
