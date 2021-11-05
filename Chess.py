#Chess
#Eitan
from asciimatics.screen import Screen
from time import sleep
#pip install asciimatics

class Board:
    royal_w = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654',  '\u2657','\u2658', '\u2656']
    royal_b = ['\u265c', '\u265e', '\u265d', '\u265b', '\u265a', '\u265d', '\u265e','\u265c']
    def __init__(self, screen): 
        self.screen = screen
        self.half_width = self.screen.width // 2
        self.half_height = self.screen.height // 2
        self.start_x = self.half_width - 20
        self.column_width = 5
        self.row_height = 3
        self.start_y = self.half_height - self.row_height * 4
        self.end_y = self.half_height + self.row_height * 4

    def draw_board(self):
        self.screen.move(self.half_width, self.half_height)
        for col in range(self.start_x, self.half_width + 21, 5):
            self.screen.move(col, 3)
            self.screen.draw(col, 27, thin=True)
        for row in range(3, 30 , 3):
            self.screen.move(self.start_x, row)
            self.screen.draw(self.half_width + 21, row, thin=True)
       
    def fill_board(self):
        for br in range(8):
            self.screen.print_at(self.royal_b[br], self.start_x + 2 + br*self.column_width, self.start_y + 1)
        for bp in range(8):
			#draw black pawns
            self.screen.print_at('\u265f', self.start_x + 2 + bp*self.column_width, self.start_y + 4)
        for wp in range(8):
			#draw white pawns
            self.screen.print_at('\u2659', self.start_x + 2 + wp*self.column_width, self.end_y - 5)    
        for wr in range(8):
			#draw white royals
            self.screen.print_at(self.royal_w[wr], self.start_x + 2 + wr*self.column_width, self.end_y - 2)        
        
def demo(screen):
    board = Board(screen)
    board.draw_board()
    board.fill_board()
    while True:
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()


Screen.wrapper(demo)


royal = ["R", '\u265E', "B", "Q", "K", "B", "N", "R"]
pawn = ["p" for x in range(8)]

def pieces(pieces, color):
    colored_pieces = [[color + p] for p in pieces]
    print(colored_pieces)


def empty_board():
    #creates an empty board
    line = [["--"] for x in range(8)] 
    pieces(royal, "W")
    pieces(pawn, "W")
    for x in range(4):
        print(line)
    pieces(pawn, "B")
    pieces(royal, "B")
#class Board:
    
