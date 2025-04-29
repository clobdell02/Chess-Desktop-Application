import pygame
import chess

from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.king import King

# Define the board colors
Light_Brown = (240, 225, 210)
Dark_Brown = (75, 63, 51)
# Screen dimension constants
square_pixel_size = 75
board_size = 8
width = 900
height = 700
label_pad = 20

# Create the game board
def draw_board(screen):
    colors = [Light_Brown, Dark_Brown]
    font = pygame.font.SysFont("Times New Roman", 20, pygame.font.Font.bold)
    # nested for loops to create 8 rows & columns of alternating colored spaces
    for row in range(8):
        for col in range(8):
            # screen is the game image, alternating colors defined withing a 75x75 pixel rectangle
            pygame.draw.rect(screen, colors[(row + col) % 2], (col * square_pixel_size + label_pad, row * square_pixel_size + label_pad, square_pixel_size, square_pixel_size))
    # create a boarder around the game board
    pygame.draw.rect(screen, (0, 0, 0), (label_pad - 5, label_pad - 5, square_pixel_size * board_size + 10, square_pixel_size * board_size + 10), 5)
    # iterate through the columns to label them a-h
    for col in range(8):
        label = chr(ord('A') + col)
        text = font.render(label, True, (0, 0, 0))
        screen.blit(text, (col * square_pixel_size + label_pad + square_pixel_size // 3, label_pad + square_pixel_size * board_size + 5))
    # repeat for the rows using 1-8
    for row in range(8):
        label = str(8 - row)
        text = font.render(label, True, (0, 0, 0))
        screen.blit(text, (label_pad - 18, row * square_pixel_size + label_pad + square_pixel_size // 3))

# Create the move history display
def draw_move_history(screen, move_history):
    font = pygame.font.SysFont("Times New Roman", 20, pygame.font.Font.bold)
    y_offset = 20
    # create the move history title
    history_title = font.render("MOVE HISTORY", True, (0, 0, 0))
    screen.blit(history_title, (width - 250 + 20, label_pad + y_offset))
    y_offset += 30 # needed so that the first move is not under the title
    # redefine font without the bold
    font = pygame.font.SysFont("Times New Roman", 20)
    # write each move into the move history display
    for i, move in enumerate(move_history):
        move_text = font.render(move, True, (0, 0, 0))
        screen.blit(move_text, (width - 250 + 20, label_pad + y_offset))
        y_offset += 30

# import the piece images into respective dictionaries based on piece color
# create a dictionary to represent the quantity and starting spot of each piece
white_pieces = {
    'wP': pygame.image.load('images/wP.svg'),
    'wR': pygame.image.load('images/wR.svg'),
    'wN': pygame.image.load('images/wN.svg'),
    'wB': pygame.image.load('images/wB.svg'),
    'wQ': pygame.image.load('images/wQ.svg'),
    'wK': pygame.image.load('images/wK.svg')
}

white_pieces_positions = {
    # loop through each column so there is 8 pawns
    'wP': [(6, i) for i in range(8)],
    # rooks, bishops, and knights all have two of the piece to start
    'wR': [(7, 0), (7, 7)],
    'wN': [(7, 1), (7, 6)],
    'wB': [(7, 2), (7, 5)],
    # each color only has one king and one queen to start
    'wQ': [(7, 3)],
    'wK': [(7, 4)]
}

black_pieces = {
    'bP': pygame.image.load('images/bP.svg'),
    'bR': pygame.image.load('images/bR.svg'),
    'bN': pygame.image.load('images/bN.svg'),
    'bB': pygame.image.load('images/bB.svg'),
    'bQ': pygame.image.load('images/bQ.svg'),
    'bK': pygame.image.load('images/bK.svg')
}

# repeat the position dictionary for the black pieces
black_pieces_positions = {
    'bP': [(1, i) for i in range(8)],
    'bR': [(0, 0), (0, 7)],
    'bN': [(0, 1), (0, 6)],
    'bB': [(0, 2), (0, 5)],
    'bQ': [(0, 3)],
    'bK': [(0, 4)]
}

# initialize the starting positions of the pieces
board = chess.Board()

# Place the game pieces on their starting positions
def draw_pieces(screen):
    # loop through the white pieces
    for piece_type, positions in white_pieces_positions.items():
        image = white_pieces[piece_type]
        # loop through the piece positions
        for position in positions:
            row, col = position
            # draw the piece at the correct position and center within the respective square
            screen.blit(image, ((col * square_pixel_size + label_pad + 15), (row * square_pixel_size + label_pad + 15)))

    # repeat the loop for the black pieces
    for piece_type, positions in black_pieces_positions.items():
        image = black_pieces[piece_type]
        for position in positions:
            row, col = position
            screen.blit(image, ((col * square_pixel_size + label_pad + 15), (row * square_pixel_size + label_pad + 15)))

def get_valid_moves_for_piece(piece_code, position):
    if piece_code == "wQ":
        return get_valid_moves(position, "white", board)
    elif piece_code == "bQ":
        return get_valid_moves(position, "black", board)
    elif piece_code == "wR":
        return get_valid_moves(position, "white", board)
    elif piece_code == "bR":
        return get_valid_moves(position, "black", board)
    elif piece_code == "wB":
        return get_valid_moves(position, "white", board)
    elif piece_code == "bB":
        return get_valid_moves(position, "black", board)
    elif piece_code == "wN":
        return get_valid_moves(position, "white", board)
    elif piece_code == "bN":
        return get_valid_moves(position, "black", board)
    elif piece_code == "wP":
        return get_valid_moves(position, "white", board)
    elif piece_code == "bP":
        return get_valid_moves(position, "black", board)
    elif piece_code == "wK":
        return get_valid_moves(position, "white", board)
    elif piece_code == "bK":
        return get_valid_moves(position, "black", board)
    else:
        raise ValueError("Invalid piece code")