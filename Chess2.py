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
RED = (255, 0, 0)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

TILE_SIZE = WIDTH // 8

class Board:
    MARGIN = 5

    def __init__(self, win):
        self.pieces = {}
        win.fill(WHITE)
        self.draw_grid(win, 8, 800)
        bp = pygame.image.load("pieces/black_pawn.png")
        bpr = pygame.transform.scale(bp, (TILE_SIZE - self.MARGIN, TILE_SIZE - self.MARGIN))
        self.pieces[(0, 0)] = bpr
        self.draw_piece(win, (0, 0), bpr)

    def draw_piece(self, win, pos, piece):
        x, y = pos_to_tile(pos)
        win.blit(piece, (x + self.MARGIN, y + self.MARGIN))


    def is_empty(self, pos):
        return not self.pieces.get(pos)


    def draw_grid(self, win, rows, width):
        gap = TILE_SIZE
        for i in range(rows):
            pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


class Tile:
    def __init__(self, pos):
        self.x, self.y = pos

    def invalid(self, win):
        self.highlight(win, RED)

    def highlight(self, win, color = YELLOW):
        pygame.draw.rect(
            win,
            color,
            pygame.Rect(self.x * TILE_SIZE + 1, self.y * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1)
        )

    def clear(self, win):
        self.highlight(win, WHITE)


class Move:
    def __init__(self, board):
        self.board = board
        self.clear()

    def is_invalid(self, pos):
        """
        The move is invalid if hasn't started and the tile is empty or
        has started and the target is a piece of the same color or
        has started and the source cannot move in that pattern
        """
        not self.source and self.board.is_empty(pos)

    def clear(self):
        self.source = None
        self.target = None

    def start(self, pos):
        self.source = pos

    def has_started_on(self, pos):
        return self.source == pos


def pos_to_tile(pos):
    x, y = pos
    return x // TILE_SIZE, y // TILE_SIZE


def highlight_tile(pos, win, move):
    bpos = pos_to_tile(pos)
    tile = Tile(bpos)

    # There's no piece in that position -> show is an error
    # The move already started on that position -> should be cleared/reset
    # The move hasn't started -> make it start on that position
    # The move has started and target is a different position -> unhighlight and move the piece
    if move.is_invalid(bpos):
        tile.invalid(win)
    elif move.has_started_on(bpos):
        tile.clear(win)
        move.clear()
    else:
        tile.highlight(win)
        move.start(bpos)

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

    pygame.display.flip()

