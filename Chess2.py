#Chess 2
#Eitan
#uses pygame

import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

board = [['  ' for i in range(8)] for i in range(8)]

WIDTH = 800

""" This is creating the window that we are playing on, it takes a tuple argument which is the dimensions of the window so in this case 800 x 800px
"""
WIN = pygame.display.set_mode((WIDTH, WIDTH))


pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

TILE_SIZE = WIDTH // 8

bp = pygame.image.load("pieces/black_pawn.png")
bpr = pygame.transform.scale(bp, (TILE_SIZE, TILE_SIZE))

def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


# board.init(WIN)
# Draws the board and the pieces
screen.fill(WHITE)
draw_grid(WIN, 8, 800)

def pos_to_tile(pos):
    x, y = pos
    return x // TILE_SIZE, y // TILE_SIZE


def highlight_tile(pos, win, board):
    print(pos)
    x, y = pos_to_tile(pos)
    print(x, y)
    pygame.draw.rect(win, YELLOW, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # Paint that tile yellow
    return board

def event_response(event):

    # Either we need to select a tile
    # Or move a piece to the tiile
    # And deselect the previous
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        return lambda win, board: highlight_tile(pos, win, board) 

    return lambda win, board: board


while 1:
    pygame.time.delay(50)

    # Some function about events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Returns a function to handle the event
        # For example clicking on unselected tile highlights the tile
        # Clicking a selected tile un-highlights the tile
        # Clicking on a tile when there's one selected attemps to move the piece to the target tile
        event_action = event_response(event)

        board = event_action(WIN, board)

    WIN.blit(bpr, (10, 10))
    pygame.display.flip()

