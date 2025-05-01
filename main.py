import pygame
import chess
from gui import visuals as viz
from src.board import Board
from src.pieces.bishop import Bishop
from src.pieces.knight import Knight
from src.pieces.king import King
from src.pieces.queen import Queen
from src.pieces.rook import Rook

#initialize the pygame window
pygame.init()

#initialize a list for the move history
move_history = []

# set up the game board
screen = pygame.display.set_mode((900, 700)) # extra width to display move history in
pygame.display.set_caption("Chess for Beginners")

# helper functions
def pos_notation(position):
    row, col = position
    row_notation = 8 - row
    col_notation = chr(ord('A') + col)
    return f"{col_notation}{row_notation}"

def get_board_position(mouse_pos):
    col = mouse_pos[0] // 75
    row = mouse_pos[1] // 75
    return row, col

def record_move(start_pos, end_pos):
    start = pos_notation(start_pos)
    end = pos_notation(end_pos)
    move_history.append(f"{start} to {end}")
    # logic to limit number of moves seen, will change to a scroll so you can see full game history
    max_moves = 20
    if len(move_history) > max_moves:
        move_history.pop(0)

def make_move(start_pos, end_pos, board):
    piece = board.get_piece_at(*start_pos) # needed for complex moves like promotion
    valid_moves = piece.get_valid_moves(board)
    for move in valid_moves:
    # check for promotion flag
        if isinstance(move, tuple) and len(move) == 2 and move[0] == 'promotion' and move[1] == end_pos: # this is a valid promotion move
            # get player input for their piece of choice, make a gui later
            prom_choice = input("Choose a promotion: (Queen, Rook, Bishop, or Knight): ").strip().lower()
            # check player input
            if prom_choice == 'bishop':
                prom_piece = Bishop(piece.color, end_pos)
            elif prom_choice == 'knight':
                prom_piece = Knight(piece.color, end_pos)
            elif prom_choice == 'queen':
                prom_piece = Queen(piece.color, end_pos)
            elif prom_choice == 'rook':
                prom_piece = Rook(piece.color, end_pos)
            else: # if invalid or no input default to a queen
                prom_piece = Queen(piece.color, end_pos)

            # simulate to see if promotion removes check
            og_target = board.get_piece_at(*end_pos)
            board.remove_piece_at(*start_pos)
            board.place_piece(prom_piece, end_pos)
            # check if king is now out of check
            king_pos = board.get_king_position(piece.color)
            king = board.get_piece_at(*king_pos)
            still_in_check = King.is_in_check(king, board) if king else True
            # if invalid undo
            if still_in_check:
                print(f"Invalid move still in check")
                board.remove_piece_at(*end_pos)
                board.place_piece(piece, start_pos)
                if og_target:
                    board.place_piece(og_target, end_pos)
                return False
            # record the promotion move
            record_move(start_pos, end_pos)
            return True
    # otherwise preform a normal move
    if end_pos in valid_moves:
        captured_piece = board.get_piece_at(*end_pos)
        board.move_piece(start_pos, end_pos)
        # check if king is now out of check
        king_pos = board.get_king_position(piece.color)
        king = board.get_piece_at(*king_pos)
        still_in_check = King.is_in_check(king, board) if king else True
        # if so invalid
        if still_in_check:
            print(f"Invalid move still in check")
            board.move_piece(end_pos, start_pos)
            if captured_piece:
                board.place_piece(captured_piece, end_pos)
            return False
        # record a valid move
        record_move(start_pos, end_pos)
        return True
    # return false as move is invalid
    return False

def gameLoop(screen):
    # set inital values for the game loop
    running = True
    current_piece = None
    moving = False
    turn = 'white'

    # initializing the board before game loop so it occurs ONCE
    board = Board()

    while running:
        # clear the screen and draw the board
        screen.fill((255, 255, 255))
        viz.draw_board(screen)
        viz.draw_move_history(screen, move_history)
        # draw the pieces on the board
        viz.draw_pieces(screen, board)

        # handle player input/moves
        if moving and current_piece:
            # moves the piece based on cursor location
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0, 0, 0), (mouse_x, mouse_y), 30)
        pygame.display.flip()

        # for loop to manage all possible events (ex: quitting, mouse clicks)
        for event in pygame.event.get():
            # if the user closes the window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # is there a left click
                    mouse_pos = pygame.mouse.get_pos()
                    row, col = get_board_position(mouse_pos)
                    # check if mouse click is on a piece or empty square
                    piece = board.get_piece_at(row, col)
                    # check if piece is selected and if its the coprrect turn color
                    if piece and piece.color == turn:
                        current_piece = piece
                        valid_moves = piece.get_valid_moves(board)
                        moving = True
            elif event.type == pygame.MOUSEMOTION:
                if moving and current_piece:
                    pass # add visual feedback for valid moves
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    row, col = get_board_position(mouse_pos)
                    #
                    if moving and current_piece:
                        if (row, col) in valid_moves:
                            valid_move = make_move(current_piece.position, (row, col), board)
                            if valid_move:
                                # switch the turn color
                                if turn == 'white':
                                    turn = 'black'
                                else:
                                    turn = 'white'
                        # reset moving and current piece
                        current_piece = None
                        moving = False

if __name__ == "__main__":
    gameLoop(screen)

pygame.quit()