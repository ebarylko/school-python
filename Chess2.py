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

INVALID = (206, 128, 112)
SELECTED = (235, 238, 151)
POSSIBLE = (152, 238, 151)


TILE_SIZE = WIDTH // 8

class Piece:
    MARGIN = 5
    def __init__(self, image_file, color):
        self.image_file = image_file
        piece = pygame.image.load(image_file)
        self.image = pygame.transform.scale(piece, (TILE_SIZE - self.MARGIN, TILE_SIZE - self.MARGIN))
        self.color = color

    def can_move_to(self, pos1, pos2):
        return False


    def draw_piece(self, pos):
        x, y = pos
        WIN.blit(
            self.image,
            (x * TILE_SIZE + self.MARGIN, y * TILE_SIZE + self.MARGIN)
        )



class Pawn(Piece):
    def can_move_to(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        hrz =abs(x2 - x1) <= 1
        if self.color == BLACK:
            return hrz and (y2 - y1 == 1 or y1 == 1 and y2 == 3 and x2 == x1)

        return hrz and (y2 - y1 == -1 or y1 == 6 and y2 == 4 and x2 == x1)



class Board:
    MARGIN = 5

    def __init__(self):
        self.draw_grid(8, 800)
        self.draw_pieces()

    def piece(self, pos):
        return self.pieces.get(pos)

    def move_piece(self, source, target):
        self.pieces[target] = self.pieces[source]
        del self.pieces[source]

    def create_pieces(self):
        pieces = {}
        for i, piece in enumerate(["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]):
            pieces[(i,0)] = Piece("pieces/black_{0}.png".format(piece), BLACK)
            pieces[(i,7)] = Piece("pieces/white_{0}.png".format(piece), WHITE)
            
        for i in range(8):
            pieces[(i, 1)] = Pawn("pieces/black_pawn.png", BLACK)
            pieces[(i, 6)] = Pawn("pieces/white_pawn.png", WHITE)
        return pieces

    def draw_pieces(self):
        self.pieces = self.create_pieces()
        for pos, piece in self.pieces.items():
            piece.draw_piece(pos)


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
        self.highlight(INVALID)

    def highlight(self, color = SELECTED, redraw = True):
        pygame.draw.rect(
            WIN,
            color,
            pygame.Rect(self.x * TILE_SIZE + 1, self.y * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1)
        )
        redraw and self.piece and self.piece.draw_piece((self.x, self.y))

    def unhighlight(self):
        self.highlight(WHITE)

    def clear(self):
        self.highlight(WHITE, False)


class Move:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def preview(self, pos, prev):
        self.check_previous(pos, prev)
        self.preview_imp(pos)


class FirstMove(Move):
    def check_previous(self, pos, prev):
        if prev and pos != prev:
            piece = self.board.piece(prev)
            Tile(prev, piece).unhighlight()


    def preview_imp(self, pos):
        piece = self.board.piece(pos)
        tile = Tile(pos, piece)
        if not piece or piece.color != self.player:
            tile.invalid()
            return

        tile.highlight(POSSIBLE)


    def accept(self, pos):
        """
        The move is invalid if is an empty tile
        and the piece doesn't match the player color
        If it is a valid move the tile should be highlighted
        and switch to wait for a second move
        """
        print(self.player)
        print("First move")
        piece = self.board.piece(pos)
        tile = Tile(pos, piece)
        if not piece or piece.color != self.player:
            return self

        tile.highlight()

        return SecondMove(self.board, self.player, pos)


class SecondMove(Move):
    def __init__(self, board, player, pos):
        self.board = board
        self.player = player
        self.first_pos = pos


    def check_previous(self, pos, prev):
        if prev and pos != prev and prev != self.first_pos:
            piece = self.board.piece(prev)
            Tile(prev, piece).unhighlight()


    def preview_imp(self, second_pos):
        piece1 = self.board.piece(self.first_pos)
        piece2 = self.board.piece(second_pos)
        tile = Tile(second_pos, piece2)

        if second_pos == self.first_pos:
            return

        if piece2 and piece2.color == self.player:
            tile.invalid()
            return

        if not piece1.can_move_to(self.first_pos, second_pos):
            tile.invalid()
            return

        tile.highlight(POSSIBLE)


    def accept(self, second_pos):
        """
        The second move is valid if it selected a piece of the other player
        or is an empty space
        and the piece can move in that pattern
        """
        print("Second move")
        piece1 = self.board.piece(self.first_pos)
        piece2 = self.board.piece(second_pos)
        tile = Tile(second_pos, piece2)
        if piece2 and piece2.color == self.player:
            return self

        if piece1.can_move_to(self.first_pos, second_pos):
            Tile(self.first_pos, None).clear()
            piece1.draw_piece(second_pos)
            self.board.move_piece(self.first_pos, second_pos)
            return FirstMove(self.board, self.next_player())

        tile.invalid()

        return self


    def next_player(self):
        if self.player == WHITE:
            return BLACK
        else:
            return WHITE



def pos_to_tile(pos):
    x, y = pos
    return x // TILE_SIZE, y // TILE_SIZE


def event_response(event, move, previous_pos):

    # Either we need to select a tile
    # Or move a piece to the tiile
    # And deselect the previous
    print(event.type)
    pos = pygame.mouse.get_pos()
    bpos = pos_to_tile(pos)
    move.preview(bpos, previous_pos)
    print(bpos)
    if event.type == pygame.MOUSEBUTTONDOWN:
        return move.accept(bpos), bpos


    return move, bpos


# Draws the board and the pieces
board = Board()

# Move to use for events
move = FirstMove(board, WHITE)
previous_pos = None
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
        move, previous_pos = event_response(event, move, previous_pos)

    pygame.display.flip()

