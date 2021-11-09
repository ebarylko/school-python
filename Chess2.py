#Chess 2
#Eitan
#uses pygame

import sys, pygame, re
pygame.init()

"""
Width and height of the board
"""
WIDTH = 800

"""
This is creating the window that we are playing on, it takes a tuple argument which is the dimensions of the window so in this case 800 x 800px
"""
WIN = pygame.display.set_mode((WIDTH, WIDTH))


pygame.display.set_caption("Chess")

"""
Colors constants
"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

INVALID = (206, 128, 112)
SELECTED = (235, 238, 151)
POSSIBLE = (152, 238, 151)

"""
Height and width of each tile
"""
TILE_SIZE = WIDTH // 8

"""
Constants for kind of moves
"""
HORIZONTAL = 1
VERTICAL = 2
DIAGONAL = 3

class Piece:
    """
    Represents the base class for a chess piece
    """

    """
    Margin to draw the pieces
    """
    MARGIN = 5

    def __init__(self, image_file, color):
        """
        Pre: Takes the image file and the color
        Post: initializes the instance of the Piece class by
        calculating the name, loading the image and resizing it
        and storing the color
        """
        self.image_file = image_file
        m = re.search('/(.+)\.', image_file)
        self.name = m.group(1)
        piece = pygame.image.load(image_file)
        self.image = pygame.transform.scale(piece, (TILE_SIZE - self.MARGIN, TILE_SIZE - self.MARGIN))
        self.color = color


    def draw_piece(self, pos):
        """
        Pre: Takes a position where the piece should be drawn
        Post: Shows the image on the screen
        """
        x, y = pos
        WIN.blit(
            self.image,
            (x * TILE_SIZE + self.MARGIN, y * TILE_SIZE + self.MARGIN)
        )


    def not_in_between(self, pos1, pos2, board):
        """
        Pre: Takes the begin and ending position for a move and the board
        Post: Returns the kind of move (HORIZONTAL, VERTICAL or DIAGONAL)
        if there's no piece between pos1 and pos2, False otherwise.
        """
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
    """
    Represents the Rook chess piece
    """

    def can_move_to(self, pos1, pos2, board):
        """
        Pre: Takes start and end position and a board,
        assumes pos2 is empty or occupied by piece of
        other color
        Post: Returns True if the kind of move is HORIZONTAL
        or VERTICAL, False otherwise.
        """
        kind = self.not_in_between(pos1, pos2, board)
        return kind in [HORIZONTAL, VERTICAL]


class Knight(Piece):
    """
    Represents the Knight chess piece
    """

    def can_move_to(self, pos1, pos2, board):
        """
        Pre: Takes start and end position and a board,
        assumes pos2 is empty or occupied by piece of
        other color
        Post: Returns True if pos2 is two ahead and one to the side
        or one ahead and two the side of pos1
        """
        x1, y1 = pos1
        x2, y2 = pos2
        diff_x = abs(x2 - x1)
        diff_y = abs(y2 - y1)
        return diff_x > 0 and diff_y > 0 and diff_x + diff_y == 3


class Bishop(Piece):
    """
    Represent the Bishop chess piece
    """

    def can_move_to(self, pos1, pos2, board):
        """
        Pre: Takes start and end position and a board,
        assumes pos2 is empty or occupied by piece of
        other color
        Post: Returns True if pos2 is diagonal to pos1 and there
        is no piece between them.
        """
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
    """
    Represents the Queen chess piece
    """

    def can_move_to(self, pos1, pos2, board):
        """
        Pre: Takes start and end position and a board,
        assumes pos2 is empty or occupied by piece of
        other color
        Post: Returns True if the pos1 and pos2 are either
        HORIZONTAL, VERTICAL or DIAGONAL.
        """
        return self.not_in_between(pos1, pos2, board)


class King(Piece):
    """
    Represents the King chess piece
    """

    def can_move_to(self, pos1, pos2, board):
        """
        Pre: Takes start and end position and a board,
        assumes pos2 is empty or occupied by piece of
        other color
        Post: Returns True if pos2 is one tile away
        from pos1 
        """
        x1, y1 = pos1
        x2, y2 = pos2
        diff_x = abs(x2 - x1)
        diff_y = abs(y2 - y1)
        return diff_x + diff_y <= 2 and diff_x + diff_y > 0 and diff_x <= 1 and diff_y <= 1


class Pawn(Piece):
    "class representing Pawn chess piece"
    def can_move_to(self, pos1, pos2, board):
        """
        Pre: Takes start and end position and a board,
        assumes pos2 is empty or occupied by piece of
        other color
        Post: Returns True if pos2 is one tile away
        (two, when it is the first move)
        from pos1 and either is diagonal and occupied,
        or vertical and empty. 
        """
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
    """
    represents a chessboard with a
    Dictionary to store pieces by coordinate
    """
    MARGIN = 5

    def __init__(self):
        """
        Pre: (none)
        Post: draws the grid and the pieces on the screen
        """
        self.draw_grid(8, 800)
        self.draw_pieces()

    def piece(self, pos):
        """
        Pre: takes a position
        Post: returns the piece in that position or None
        """
        return self.pieces.get(pos)

    def move_piece(self, source, target):
        """
        Pre: takes a source and target position
        Post: assigns the piece in source to target,
        clears source position in the board
        """
        self.pieces[target] = self.pieces[source]
        del self.pieces[source]

    def create_pieces(self):
        """
        Pre: (none)
        Post: returns a dictionary with the pieces in their places
        """
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
        """
        Pre: (none)
        Post: creates the pieces and draws each one
        on the board"""
        self.pieces = self.create_pieces()
        for pos, piece in self.pieces.items():
            piece.draw_piece(pos)


    def draw_grid(self, rows, width):
        """
        Pre: takes how many rows and a value for
        the width
        Post: draws a grid on the screen
        """
        WIN.fill(WHITE)
        gap = TILE_SIZE
        for i in range(rows):
            pygame.draw.line(WIN, BLACK, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(WIN, BLACK, (j * gap, 0), (j * gap, width))


class Tile:
    """
    represents a tile in the board
    """
    def __init__(self, pos, piece):
        """
        Pre: takes a position and a piece
        Post: stores the position and piece in the instance
        """
        self.x, self.y = pos
        self.piece = piece

    def invalid(self):
        """
        Pre: (none)
        Post: highlights the position of the tile as invalid
        """
        self.highlight(INVALID)

    def highlight(self, color = SELECTED, redraw = True):
        """
        Pre: takes a color constant and a flag to redraw the piece
        Post: highlights a rectangle on the screen with the given
        color and draws the piece on top if the redraw flag is True
        """
        pygame.draw.rect(
            WIN,
            color,
            pygame.Rect(self.x * TILE_SIZE + 1, self.y * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1)
        )
        redraw and self.piece and self.piece.draw_piece((self.x, self.y))

    def unhighlight(self):
        """
        Pre: (none)
        Post: clears the square and redraws the piece
        """
        self.highlight(WHITE)

    def clear(self):
        """
        Pre: (none)
        Post: clears the square(paints it white)
        """
        self.highlight(WHITE, False)


class Move:
    """
    Base class for representing a move
    """
    def __init__(self, board, player):
        """
        Pre: takes a board and a player
        Post: stores the board and player in instance
        """
        self.board = board
        self.player = player

    def cancel(self):
        """
        Pre: (none)
        Post: returns an instance of first move (no piece selected)
        """
        print("Back to selection")
        return FirstMove(self.board, self.player)

    def preview(self, pos, prev):
        """
        Pre: takes a position and the previous previewed position
        Post: highlights tile to indicate if it is a possible move
        """
        self.check_previous(pos, prev)
        self.preview_imp(pos)


class FirstMove(Move):
    """
    Represents piece selection before deciding destination
    """
    def check_previous(self, pos, prev):
        """
        Pre: takes current and previous position
        Post: if there is a previous position and it differs
        from the current one, unhighlights previous position
        """
        if prev and pos != prev:
            piece = self.board.piece(prev)
            Tile(prev, piece).unhighlight()


    def preview_imp(self, pos):
        """
        Pre:takes a position
        Post: highlights the position as a possible option unless
        the position has no piece or has a piece but is of a
        different color from the current player
        """
        piece = self.board.piece(pos)
        tile = Tile(pos, piece)
        if not piece or piece.color != self.player:
            tile.invalid()
            return

        tile.highlight(POSSIBLE)


    def accept(self, pos):
        """
        Pre: takes a position
        Post: Returns the same first move if there is no piece in
        that position or the piece color doesn't match the current player.
        Otheriwse highlights the current position as selected
        and returns a second move instance to wait for the destination.
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
    """
    Represents the move after selecting the piece in the board
    """

    def __init__(self, board, player, pos):
        """
        Pre: Takes a board a player color and a position
        Post: Stores the board, the player and the position as the first position
        """
        self.board = board
        self.player = player
        self.first_pos = pos

    def cancel(self):
        """
        Pre: (none)
        Post: Unhighlights the selection and calls the parent
        cancel to return a first move (back to selection).
        """
        piece1 = self.board.piece(self.first_pos)
        Tile(self.first_pos, piece1).unhighlight()
        return super().cancel()

    def check_previous(self, pos, prev):
        """
        Pre: Takes a postition and a previous previewed position
        Post: Unhighlights the previous position unless
        it does not exists or the current and previous position are the same 
        or is the first position selected in the previous move
        """
        if prev and pos != prev and prev != self.first_pos:
            piece = self.board.piece(prev)
            Tile(prev, piece).unhighlight()


    def preview_imp(self, second_pos):
        """
        Pre: takes a position (the target of the first)
        Post: Shows the second position as a possible option
        if is different from the first position selected
        and there is a piece of a different color
        and the piece in the first position can move to the second.
        Otherwise shows the second position as invalid.
        """
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
        Pre: Takes the second position of the move
        Post: Returns a first move for the other player with
        the board updated to reflect the new position or the piece taken if valid.
        If the move is invalid returns the same second move instance (does nothing).
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
        """
        Pre: (none)
        Returns: White player if current player is black, black otherwise.
        """
        if self.player == WHITE:
            return BLACK
        else:
            return WHITE



def pos_to_tile(pos):
    """
    Pre: A position in pixel coordinates
    Post: A position of the chess board using TILE_SIZE
    to identify the row and the column
    """
    x, y = pos
    return x // TILE_SIZE, y // TILE_SIZE


def event_response(event, move, previous_pos):
    """
    Pre: Takes an event, the current move and the previous position
    Post: Returns a pair (move, board_pos).
    The board position is calculated based on the position of the mouse.
    If the player presses the ESC key cancels the move going back to selection.
    If the user selects a board tile, asks the move to accept the selection
    and returns the updated move
    (first move (current player) -> second move -> first move (next player) -> and so on)
    """

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


"""
Instance of the board
"""
board = Board()

"""
Starts the white player waiting for a first move
"""
move = FirstMove(board, WHITE)

"""
There is no previous position
"""
previous_pos = None

"""
The game is starting!
"""
print("White pieces turn")


"""
Infinite loop waiting for events
Quitting the application will stop the loop
"""
while 1:
    # Small delay to avoid killing the CPU
    pygame.time.delay(50)

    # For every event
    for event in pygame.event.get():

        # Quit if quitting
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Returns a function to handle the event
        # For example clicking on unselected tile highlights the tile
        # Clicking a selected tile un-highlights the tile
        # Clicking on a tile when there's one selected attemps to move the piece to the target tile
        move, previous_pos = event_response(event, move, previous_pos)

    # Refresh the screen
    pygame.display.flip()

