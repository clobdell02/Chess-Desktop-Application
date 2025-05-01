from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.queen import Queen
from src.pieces.rook import Rook

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.load_piece_objects()

    def load_piece_objects(self):
        for col in range(8): # place pawns on the second and seventh rows, one per column
            self.grid[6][col] = Pawn('white', (6, col))
            self.grid[1][col] = Pawn('black', (1, col))
        # place the rooks
        self.grid[7][0] = Rook('white', (7, 0))
        self.grid[7][7] = Rook('white', (7, 7))
        self.grid[0][0] = Rook('black', (0, 0))
        self.grid[0][7] = Rook('black', (0, 7))
        # place the knights
        self.grid[7][1] = Knight('white', (7, 1))
        self.grid[7][6] = Knight('white', (7, 6))
        self.grid[0][1] = Knight('black', (0, 1))
        self.grid[0][6] = Knight('black', (0, 6))
        # place the bishops
        self.grid[7][2] = Bishop('white', (7, 2))
        self.grid[7][5] = Bishop('white', (7, 5))
        self.grid[0][2] = Bishop('black', (0, 2))
        self.grid[0][5] = Bishop('black', (0, 5))
        # place the queens and kings
        # queens are placed on the same color square as their color
        self.grid[7][3] = Queen('white', (7, 3))
        self.grid[0][3] = Queen('black', (0, 3))
        self.grid[7][4] = King('white', (7, 4))
        self.grid[0][4] = King('black', (0, 4))
    
    def remove_piece_at(self, row, col):
        self.grid[row][col] = None

    def place_piece(self, piece, position):
        row, col = position
        self.grid[row][col] = piece

    def get_piece_at(self, row, col):
        # check for an out of board click
        if not(0 <= row < 8 and 0 <= col < 8):
            print(f"Error: Attempted to access an out-of-bounds position: ({row}, {col})")
            return None
        else:
            return self.grid[row][col]

    def get_king_position(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece and isinstance(piece, King) and piece.color == color:
                    return(row, col)
        return None

    def move_piece(self, start, end):
        piece = self.get_piece_at(*start)
        if piece: # ensures a piece exists
            print(f"Moving {piece.color} {piece.__class__.__name__}, from {start} to {end}")
            self.grid[end[0]][end[1]] = piece
            self.grid[start[0]][start[1]] = None
            piece.position = end
        else:
            print(f"no piece found at {start}")

    def get_valid_moves(self, row, col):
        print("calling get_valid_moves from board.py")
        piece = self.get_piece_at(row, col)
        if piece:
            return piece.get_valid_moves(self)
        return []

