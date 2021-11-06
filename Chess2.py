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


while 1:
    pygame.time.delay(50) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(WHITE)
    draw_grid(WIN, 8, 800)
    WIN.blit(bpr, (10, 10))
    pygame.display.flip()

