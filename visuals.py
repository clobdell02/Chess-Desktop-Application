import pygame
from board import Board

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

# handling of the rendering of the pieces
def draw_pieces(screen, board):
    for row in range(8):  # Loop through rows
        for col in range(8):  # Loop through columns
            piece = board.get_piece_at(row, col)  # Get the piece at (row, col)
            if piece:  # If there is a piece at this position
                # Draw the piece at the calculated position
                screen.blit(piece.image, (col * square_pixel_size + label_pad + 15, row * square_pixel_size + label_pad + 15))