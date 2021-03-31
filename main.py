import pygame
from Board import board, draw_board, number, alphabets, pos
from Chess_Pieces.pieces import Black, White


WIDTH = 800
HEIGHT = WIDTH
BOX = WIDTH // 8

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


win = pygame.display.set_mode((WIDTH, HEIGHT))

board(WIDTH)
draw_board(win)
black_pieces = Black()
white_pieces = White()

def draw(win):
    black_pieces.draw_pieces(win)
    white_pieces.draw_pieces(win)
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(win)


if __name__ == "__main__":
    main()
