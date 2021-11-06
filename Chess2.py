#Chess 2
#Eitan
#uses pygame

import sys, pygame
pygame.init()


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

class Board:

    def __init__(self, win):
        self.pieces = {}
        win.fill(WHITE)
        self.draw_grid(win, 8, 800)

    def draw_grid(self, win, rows, width):
        gap = TILE_SIZE
        for i in range(rows):
            pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


class Tile:
    def __init__(self, pos):
        self.x, self.y = pos

    def highlight(self, win):
        pygame.draw.rect(
            win,
            YELLOW,
            pygame.Rect(self.x * TILE_SIZE + 1, self.y * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1)
        )

    def unhighlight(self, win):
        pygame.draw.rect(
            win,
            WHITE,
            pygame.Rect(self.x * TILE_SIZE + 1, self.y * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1)
        )


class Move:

    def __init__(self, board):
        self.board = board
        self.clear()


    def clear(self):
        self.source = None
        self.target = None

    def select(self, pos):
        self.source = pos

    def is_selected(self, pos):
        return self.source == pos


def pos_to_tile(pos):
    x, y = pos
    return x // TILE_SIZE, y // TILE_SIZE


def highlight_tile(pos, win, move):
    bpos = pos_to_tile(pos)
    tile = Tile(bpos)
    if move.is_selected(bpos):
        tile.unhighlight(win)
        move.clear()
    else:
        tile.highlight(win)
        move.select(bpos)

    return move


def event_response(event):

    # Either we need to select a tile
    # Or move a piece to the tiile
    # And deselect the previous
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        return lambda win, move: highlight_tile(pos, win, move)

    return lambda win, move: move


# Draws the board and the pieces
board = Board(WIN)

# Move to use for events
move = Move(board)

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

        move = event_action(WIN, move)

    WIN.blit(bpr, (10, 10))
    pygame.display.flip()

