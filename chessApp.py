import chess
import pygame

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess for beginers")

# Define the board colors
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)

# Create the game board
def draw_board():
    colors = [WHITE, BLACK]
    # nested for loops to create 8 rows & columns of alternating colored spaces
    for row in range(8):
        for col in range(8):
            # screen is the game image, alternating colors defined withing a 75x75 pixel rectangle
            pygame.draw.rect(screen, colors[(row + col) % 2], (col * 75, row * 75, 75, 75))

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
    pygame.display.flip()

pygame.quit()