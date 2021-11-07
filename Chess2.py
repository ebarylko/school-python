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

class Piece:
    MARGIN = 5
    def __init__(self, image_file, color):
        self.image_file = image_file
        piece = pygame.image.load(image_file)
        self.image = pygame.transform.scale(piece, (TILE_SIZE - self.MARGIN, TILE_SIZE - self.MARGIN))
        self.color = color

    def can_move_to(self, pos):
        return True

    def draw_piece(self, pos):
        x, y = pos
        WIN.blit(
            self.image,
            (x * TILE_SIZE + self.MARGIN, y * TILE_SIZE + self.MARGIN)
        )


class Board:
    MARGIN = 5

    def __init__(self):
        self.draw_grid(8, 800)
        self.draw_pieces()

    def piece(self, pos):
        return self.pieces.get(pos)

    def create_pieces(self):
        pieces = {}
        for i in range(8):
            pieces[(i, 1)] = Piece("pieces/black_pawn.png", BLACK)
            pieces[(i, 6)] = Piece("pieces/black_pawn.png", WHITE)
        return pieces

    def draw_pieces(self):
        self.pieces = self.create_pieces()
        for pos, piece in self.pieces.items():
            piece.draw_piece(pos)



    def is_empty(self, pos):
        return not self.pieces.get(pos)


    def draw_grid(self, rows, width):
        WIN.fill(WHITE)
        gap = TILE_SIZE
        for i in range(rows):
            pygame.draw.line(WIN, BLACK, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(WIN, BLACK, (j * gap, 0), (j * gap, width))


class Tile:
    def __init__(self, pos, piece):
        self.x, self.y = pos
        self.piece = piece

    def invalid(self):
        self.highlight(RED)

    def highlight(self, color = YELLOW, redraw = True):
        pygame.draw.rect(
            WIN,
            color,
            pygame.Rect(self.x * TILE_SIZE + 1, self.y * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1)
        )
        redraw and self.piece and self.piece.draw_piece((self.x, self.y))

    def clear(self):
        self.highlight(WHITE, False)


class FirstMove:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def accept(self, pos):
        """
        The move is invalid if is an empty tile
        and the piece doesn't match the player color
        If it is a valid move the tile should be highlighted
        and switch to wait for a second move
        """
        print("First move")
        piece = self.board.piece(pos)
        tile = Tile(pos, piece)
        if not piece or piece.color != self.player:
            tile.invalid()
            return self

        tile.highlight()

        return SecondMove(self.board, self.player, pos)

class SecondMove:
    def __init__(self, board, player, pos):
        self.board = board
        self.player = player
        self.firstPos = pos


    def accept(self, secondPos):
        """
        The second move is valid if it selected a piece of the other player
        or is an empty space
        and the piece can move in that pattern
        """
        print("Second move")
        piece1 = self.board.piece(self.firstPos)
        piece2 = self.board.piece(secondPos)
        tile = Tile(secondPos, piece2)
        if piece2 and piece2.color == self.player:
            tile.invalid()
            return self

        if not piece2 and piece1.can_move_to(secondPos):
            Tile(self.firstPos, None).clear()
            piece1.draw_piece(secondPos)
            #self.board.move_piece(firstPos, pos)

        return FirstMove(self.board, self.next_player())

    def next_player(self):
        if self.player == WHITE:
            return BLACK
        else:
            return WHITE
        


def pos_to_tile(pos):
    x, y = pos
    return x // TILE_SIZE, y // TILE_SIZE


def event_response(event):

    # Either we need to select a tile
    # Or move a piece to the tiile
    # And deselect the previous
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        bpos = pos_to_tile(pos)
        return lambda move: move.accept(bpos)

    return lambda move: move


# Draws the board and the pieces
board = Board()

# Move to use for events
move = FirstMove(board, WHITE)

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

        move = event_action(move)

    pygame.display.flip()

