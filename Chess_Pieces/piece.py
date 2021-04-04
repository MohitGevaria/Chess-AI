import pygame
import sys

PATH_CHANGE = r"C:\Users\mohit\Documents\pygame Projects\CHESS_AI"
sys.path.append(PATH_CHANGE)

from Board import board, pos,pos_color,pos_reverse
board(800)
pos_reverse={y:x for x,y in pos.items()}


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 216, 230)
GREY = (128, 128, 128)
RED = (255, 0, 0)

class piece:

    def __init__(self, img_dir):
        self.img = pygame.image.load(img_dir)
        self.img=pygame.transform.scale(self.img,(80,80))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        

    def draw(self, win, x, y):
        x = x - self.width // 2
        y = y - self.height // 2
        win.blit(self.img, (x, y))

    def erase(self,win,position):
        if pos_color[pos_reverse[position]] == 0 :
            surface = pygame.Surface((100, 100))
            surface.fill(WHITE)
            win.blit(surface, (position[0] - 100 // 2, position[1] - 100 // 2))
        else:
            surface = pygame.Surface((100, 100))
            surface.fill(GREY)
            win.blit(surface, (position[0] - 100 // 2, position[1] - 100 // 2))

        

    def possible_draw(self,win,possible, possible_kill):
        for  i in possible:
            # surface= pygame.draw.rect(win, BLUE, pygame.Rect(i[0]-50, i[1]-50, i[0]+50, i[1] + 50))
            surface = pygame.Surface((100, 100))
            surface.fill(BLUE)
            surface.set_alpha(160)
            win.blit(surface, (i[0] - 100 // 2, i[1] - 100 // 2)) 
        for  i in possible_kill:
            # surface= pygame.draw.rect(win, BLUE, pygame.Rect(i[0]-50, i[1]-50, i[0]+50, i[1] + 50))
            surface = pygame.Surface((100, 100))
            surface.fill(RED)
            surface.set_alpha(160)
            win.blit(surface, (i[0] - 100 // 2, i[1] - 100 // 2)) 

    def end_of_board(self, xpos, ypos):

        if(xpos>0 and xpos<800) and (ypos>0 and ypos<800):
            return True
        else:
            return False

if __name__ == "__main__":
    print(pos_reverse)