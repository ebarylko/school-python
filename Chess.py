#Chess
#Eitan
from asciimatics.screen import Screen
from time import sleep
#pip install asciimatics

def demo(screen):
    screen.print_at('Hello world!', 0, 0)
    screen.print_at(screen.height, 30, 0)
    screen.print_at(screen.width, 70, 0)
    half_width = screen.width // 2
    half_height = screen.height // 2
    screen.move(half_width, half_height)
    start_x = half_width - 20
    column_width = 5
    row_height = 3
    start_y = half_height - row_height * 4
    while True:
        for col in range(half_width - 20, half_width + 21, 5):
            screen.move(col, 3)
            screen.draw(col, 27, thin=True)
        for row in range(3, 30 , 3):
            screen.move(half_width - 20, row)
            screen.draw(half_width + 21, row, thin=True)
        for p in range(8):
            screen.print_at('\u265f', start_x + 2 + p*column_width, start_y + 4)
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
    
