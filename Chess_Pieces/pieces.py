# from abc import ABC,abstractmethod
import pygame
import os
import sys

PATH_CHANGE = r"C:\Users\mohit\Documents\pygame Projects\CHESS_AI"
sys.path.append(PATH_CHANGE)

from Board import board, pos

board(800)



class piece:
    def __init__(self, img_dir):
        self.img = pygame.image.load(img_dir)
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def draw(self, win, x, y):
        x = x - self.width // 2
        y = y - self.height // 2
        win.blit(self.img, (x, y))

    def erase():
        pass


class King(piece):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y

    def draw(self, win):
        super().draw(win, self.x, self.y)

    def move(newx, newy):
        self.x = newx
        self.y = newy

    def name():
        return "king"


class Queen(piece):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y

    def draw(self):
        super().draw(self.x, self.y)

    def move(newx, newy):
        self.x = newx
        self.y = newy

    def name():
        return "queen"


class Rook(piece):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y

    def draw(self):
        super().draw(self.x, self.y)

    def move(newx, newy):
        self.x = newx
        self.y = newy

    def name():
        return "rook"


class Bishop(piece):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y

    def draw(self):
        super().draw(self.x, self.y)

    def move(newx, newy):
        self.x = newx
        self.y = newy

    def name():
        return "bishop"


class Knight(piece):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y

    def draw(self):
        super().draw(self.x, self.y)

    def move(newx, newy):
        self.x = newx
        self.y = newy

    def name():
        return "knight"


class Pawn(piece):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y

    def draw(self):
        super().draw(self.x, self.y)

    def move(newx, newy):
        self.x = newx
        self.y = newy

    def name():
        return "pawn"


class Black:

    path = PATH_CHANGE+"\Images"
    king_img = os.path.join(path, "black_king.png")
    queen_img = os.path.join(path, "black_queen.png")
    rook_img = os.path.join(path, "black_rook.png")
    bishop_img = os.path.join(path, "black_bishop.png")
    knight_img = os.path.join(path, "black_knight.png")
    pawn_img = os.path.join(path, "black_pawn.png")
    
    def __init__(self):
        self.list = {
            pos["e8"]: King(pos["e8"][0], pos["e8"][1], self.king_img),
            pos["d8"]: King(pos["d8"][0], pos["d8"][1], self.queen_img),
            pos["c8"]: King(pos["c8"][0], pos["c8"][1], self.bishop_img),
            pos["f8"]: King(pos["f8"][0], pos["f8"][1], self.bishop_img),
            pos["b8"]: King(pos["b8"][0], pos["b8"][1], self.knight_img),
            pos["g8"]: King(pos["g8"][0], pos["g8"][1], self.knight_img),
            pos["a8"]: King(pos["a8"][0], pos["a8"][1], self.rook_img),
            pos["h8"]: King(pos["h8"][0], pos["h8"][1], self.pawn_img),
            pos["a7"]: King(pos["a7"][0], pos["a7"][1], self.pawn_img),
            pos["b7"]: King(pos["b7"][0], pos["b7"][1], self.pawn_img),
            pos["c7"]: King(pos["c7"][0], pos["c7"][1], self.pawn_img),
            pos["d7"]: King(pos["d7"][0], pos["d7"][1], self.pawn_img),
            pos["e7"]: King(pos["e7"][0], pos["e7"][1], self.pawn_img),
            pos["f7"]: King(pos["f7"][0], pos["f7"][1], self.pawn_img),
            pos["g7"]: King(pos["g7"][0], pos["g7"][1], self.pawn_img),
            pos["h7"]: King(pos["h7"][0], pos["h7"][1], self.pawn_img),
        }
        self.name_list = []

    def getpositin(self, xold, yold, xnew, ynew):
        self.list[(xold, yold)], move()

    def draw_pieces(self, win):
        for key, value in self.list.items():
            value.draw(win)

class White:

    path = PATH_CHANGE+"\Images"
    king_img = os.path.join(path, "white_king.png")
    queen_img = os.path.join(path, "white_queen.png")
    rook_img = os.path.join(path, "white_rook.png")
    bishop_img = os.path.join(path, "white_bishop.png")
    knight_img = os.path.join(path, "white_knight.png")
    pawn_img = os.path.join(path, "white_pawn.png")
    
    def __init__(self):
        self.list = {
            pos["e1"]: King(pos["e1"][0], pos["e1"][1], self.king_img),
            pos["d1"]: King(pos["d1"][0], pos["d1"][1], self.queen_img),
            pos["c1"]: King(pos["c1"][0], pos["c1"][1], self.bishop_img),
            pos["f1"]: King(pos["f1"][0], pos["f1"][1], self.bishop_img),
            pos["b1"]: King(pos["b1"][0], pos["b1"][1], self.knight_img),
            pos["g1"]: King(pos["g1"][0], pos["g1"][1], self.knight_img),
            pos["a1"]: King(pos["a1"][0], pos["a1"][1], self.rook_img),
            pos["h1"]: King(pos["h1"][0], pos["h1"][1], self.pawn_img),
            pos["a2"]: King(pos["a2"][0], pos["a2"][1], self.pawn_img),
            pos["b2"]: King(pos["b2"][0], pos["b2"][1], self.pawn_img),
            pos["c2"]: King(pos["c2"][0], pos["c2"][1], self.pawn_img),
            pos["d2"]: King(pos["d2"][0], pos["d2"][1], self.pawn_img),
            pos["e2"]: King(pos["e2"][0], pos["e2"][1], self.pawn_img),
            pos["f2"]: King(pos["f2"][0], pos["f2"][1], self.pawn_img),
            pos["g2"]: King(pos["g2"][0], pos["g2"][1], self.pawn_img),
            pos["h2"]: King(pos["h2"][0], pos["h2"][1], self.pawn_img),
        }
        self.name_list = []

    def getpositin(self, xold, yold, xnew, ynew):
        self.list[(xold, yold)], move()

    def draw_pieces(self, win):
        for key, value in self.list.items():
            value.draw(win)