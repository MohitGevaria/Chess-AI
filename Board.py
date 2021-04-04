import pygame


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

number = list(map(str, [i for i in reversed(range(1, 9))]))
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h"]
pos = {}
pos_color = {}
pos_reverse = {}
box = 0
unique = [i for i in range(0,900,100)]



def board(width):
    global box
    global pos_reverse
    box = width // 8
    y = width // (8 * 2)
    for i in number:
        x = width // (8 * 2)
        for j in alphabets:
            pos[j + i] = (x, y)
            x += box
        y += box
    pos_reverse={y:x for x,y in pos.items()}
         
    


def draw_board(win):
    intial_color = 0
    for i in alphabets:
        current_color = intial_color

        for j in number:
            x, y = pos[i + j]
            x -= box // 2
            y -= box // 2

            if current_color == 0:
                pygame.draw.rect(win, WHITE, pygame.Rect(x, y, x + box, y + box))
                pos_color[i + j] = 0
                current_color = 1
            else:
                pygame.draw.rect(win, GREY, pygame.Rect(x, y, x + box, y + box))
                pos_color[i + j] = 1
                current_color = 0

        if intial_color == 0:
            intial_color = 1

        else:
            intial_color = 0
    pygame.display.update()

if __name__=="__main__":
    board(800)
    print(pos_reverse)