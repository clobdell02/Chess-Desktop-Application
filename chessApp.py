import pygame
import chess

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess for Beginners")

# Define the board colors
Light_Brown = (240, 225, 210)
Dark_Brown = (75, 63, 51)

# Create the game board
def draw_board():
    colors = [Light_Brown, Dark_Brown]
    # nested for loops to create 8 rows & columns of alternating colored spaces
    for row in range(8):
        for col in range(8):
            # screen is the game image, alternating colors defined withing a 75x75 pixel rectangle
            pygame.draw.rect(screen, colors[(row + col) % 2], (col * 75, row * 75, 75, 75))

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
def draw_pieces():
    # loop through the white pieces
    for piece_type, positions in white_pieces_positions.items():
        image = white_pieces[piece_type]
        # loop through the piece positions
        for position in positions:
            row, col = position
            # draw the piece at the correct position and center within the respective square
            screen.blit(image, ((col * 75 + 15), (row * 75 + 15)))

    # repeat the loop for the black pieces
    for piece_type, positions in black_pieces_positions.items():
        image = black_pieces[piece_type]
        for position in positions:
            row, col = position
            screen.blit(image, ((col * 75 + 15), (row * 75 + 15)))

# Main Game Loop
running = True
while running:
    # for loop to manage all possible events (ex: quitting, mouse clicks)
    for event in pygame.event.get():
        # if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    draw_board()
    draw_pieces()
    pygame.display.flip()

pygame.quit()