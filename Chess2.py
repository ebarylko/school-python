#Chess 2
#Eitan
#uses pygame

import sys, pygame, re
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

HORIZONTAL = 1
VERTICAL = 2
DIAGONAL = 3

class Piece:
    MARGIN = 5
    def __init__(self, image_file, color):
        self.image_file = image_file
        m = re.search('/(.+)\.', image_file)
        self.name = m.group(1)
        piece = pygame.image.load(image_file)
        self.image = pygame.transform.scale(piece, (TILE_SIZE - self.MARGIN, TILE_SIZE - self.MARGIN))
        self.color = color

    def can_move_to(self, pos1, pos2, board):
        return False


    def draw_piece(self, pos):
        x, y = pos
        WIN.blit(
            self.image,
            (x * TILE_SIZE + self.MARGIN, y * TILE_SIZE + self.MARGIN)
        )


    def not_in_between(self, pos1, pos2, board):
        x1, y1 = pos1
        x2, y2 = pos2
        diff_x = abs(x2 - x1)
        diff_y = abs(y2 - y1)

        if diff_x > 0 and diff_y== 0:
            a, b = sorted([x1, x2])
            return not [board.piece((x, y1)) for x in range(a + 1, b) if board.piece((x, y1))] and HORIZONTAL

        if diff_x == 0 and diff_y > 0:
            a, b = sorted([y1, y2])
            return not [board.piece((x1, y)) for y in range(a + 1, b) if board.piece((x1, y))] and VERTICAL

        sign = lambda a: (a>0) - (a<0)
        x_inc = sign(x2 - x1)
        y_inc = sign(y2 - y1)
        return diff_x == diff_y and not [board.piece((x1 + i * x_inc, y1 + i * y_inc)) for i in range(1, diff_x) if board.piece((x1 + i * x_inc, y1 + i * y_inc))] and DIAGONAL


class Rook(Piece):
    def can_move_to(self, pos1, pos2, board):
        kind = self.not_in_between(pos1, pos2, board)
        return kind in [HORIZONTAL, VERTICAL]


class Knight(Piece):
    def can_move_to(self, pos1, pos2, board):
        x1, y1 = pos1
        x2, y2 = pos2
        diff_x = abs(x2 - x1)
        diff_y = abs(y2 - y1)
        return diff_x > 0 and diff_y > 0 and diff_x + diff_y == 3


class Bishop(Piece):
    def can_move_to(self, pos1, pos2, board):
        x1, y1 = pos1
        x2, y2 = pos2
        sign = lambda a: (a>0) - (a<0)
        x_inc = sign(x2 - x1)
        y_inc = sign(y2 - y1)
        diff_x = abs(x2 - x1)
        diff_y = abs(y2 - y1)
        in_between = [board.piece((x1 + i * x_inc, y1 + i * y_inc)) for i in range(1, diff_x) if board.piece((x1 + i * x_inc, y1 + i * y_inc))]

        return diff_x == diff_y and not in_between


class Queen(Piece):
    def can_move_to(self, pos1, pos2, board):
        return self.not_in_between(pos1, pos2, board)


class King(Piece):
    def can_move_to(self, pos1, pos2, board):
        x1, y1 = pos1
        x2, y2 = pos2
        diff_x = abs(x2 - x1)
        diff_y = abs(y2 - y1)
        return diff_x + diff_y <= 2 and diff_x + diff_y > 0 and diff_x <= 1 and diff_y <= 1


class Pawn(Piece):
    def can_move_to(self, pos1, pos2, board):
        x1, y1 = pos1
        x2, y2 = pos2
        diff_x = x2 - x1
        diff_y = y2 -y1

        piece = board.piece((x2, y2))

        other = BLACK
        is_ahead = diff_x == 0 and (diff_y == -1 or (y1 == 6 and y2 == 4))
        is_diagonal = abs(diff_x) == 1 and diff_y == -1

        if self.color == BLACK:
            other = WHITE
            is_ahead = diff_x == 0 and (diff_y == 1 or (y1 == 1 and y2 == 3))
            is_diagonal = abs(diff_x) == 1 and diff_y == 1

        return (piece and piece.color == other and is_diagonal) or (not piece and is_ahead)




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
        royals = [("rook", Rook), ("knight", Knight), ("bishop", Bishop), ("queen", Queen), ("king", King), ("bishop", Bishop), ("knight", Knight), ("rook", Rook)]

        for i, (piece, klass) in enumerate(royals):
            pieces[(i,0)] = klass("pieces/black_{0}.png".format(piece), BLACK)
            pieces[(i,7)] = klass("pieces/white_{0}.png".format(piece), WHITE)

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

    def cancel(self):
        print("Back to selection")
        return FirstMove(self.board, self.player)

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
        piece = self.board.piece(pos)
        tile = Tile(pos, piece)
        if not piece or piece.color != self.player:
            return self

        tile.highlight()
        print("Selected ", piece.name, pos)
        print("Choose destination ")

        return SecondMove(self.board, self.player, pos)


class SecondMove(Move):
    def __init__(self, board, player, pos):
        self.board = board
        self.player = player
        self.first_pos = pos

    def cancel(self):
        piece1 = self.board.piece(self.first_pos)
        Tile(self.first_pos, piece1).unhighlight()
        return super().cancel()

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

        if not piece1.can_move_to(self.first_pos, second_pos, self.board):
            tile.invalid()
            return

        tile.highlight(POSSIBLE)


    def accept(self, second_pos):
        """
        The second move is valid if it selected a piece of the other player
        or is an empty space
        and the piece can move in that pattern
        """
        piece1 = self.board.piece(self.first_pos)
        piece2 = self.board.piece(second_pos)
        tile = Tile(second_pos, piece2)
        if piece2 and piece2.color == self.player:
            return self

        if piece1.can_move_to(self.first_pos, second_pos, self.board):
            Tile(self.first_pos, None).clear()
            piece1.draw_piece(second_pos)
            self.board.move_piece(self.first_pos, second_pos)
            print("Moved to ", second_pos)
            if self.next_player() == WHITE:
                print("Next White pieces turn")
            else:
                print("Next Black pieces turn")
            return FirstMove(self.board, self.next_player())

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
    pos = pygame.mouse.get_pos()
    bpos = pos_to_tile(pos)
    move.preview(bpos, previous_pos)

    if event.type == pygame.KEYDOWN:
        # If pressed key is ESC cancel selection
        if event.key == pygame.K_ESCAPE:
            return move.cancel(), bpos

    if event.type == pygame.MOUSEBUTTONDOWN:
        return move.accept(bpos), bpos


    return move, bpos


# Draws the board and the pieces
board = Board()

# Move to use for events
move = FirstMove(board, WHITE)

previous_pos = None

print("White pieces turn")


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

