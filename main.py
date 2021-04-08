import pygame
from Board import board, draw_board, number, alphabets, pos, unique
from Chess_Pieces.initialize_pieces import init_pieces


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
load_pieces = init_pieces()



def mouse_click(x, y):
    for i in range(len(unique)-1):
        if unique[i]<x and unique[i+1]>x:
            xpos = (unique[i]+unique[i+1])//2
        if unique[i]<y and unique[i+1]>y:
            ypos = (unique[i]+unique[i+1])//2
    return (xpos,ypos)

def draw(win):
    load_pieces.draw(win)
    pygame.display.update()
    


def main():
    run = True
    apos=0
    bpos=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    xpos, ypos = pygame.mouse.get_pos()
                    xpos, ypos = mouse_click(xpos,ypos)
                    #load_pieces.move_position(xpos,ypos)
                    
                    if(xpos,ypos) in load_pieces:
                        if xpos == apos and ypos == bpos:
                            continue
                        if xpos != apos or ypos != bpos:
                            
                            load_pieces.possible_draw_remove(win)
                            apos,bpos=xpos,ypos

                        load_pieces.possible_draw(win)
                        

                    load_pieces.move_piece(win, xpos , ypos)
                    load_pieces.checking_condition()
        
                        
        draw(win)


if __name__ == "__main__":
    main()
