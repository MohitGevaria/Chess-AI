import pygame
import os
import sys

PATH_CHANGE = r"C:\Users\mohit\Documents\pygame Projects\CHESS_AI"
PATH_CHANGE1 = r"C:\Users\mohit\Documents\pygame Projects\CHESS_AI\Chess_Pieces"
sys.path.append(PATH_CHANGE)
sys.path.append(PATH_CHANGE1)
from king import King
from queen import Queen
from rook import  Rook
from bishop import Bishop
from knight import Knight
from pawn import Pawn

from Board import board, pos,pos_color,pos_reverse

board(800)
BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

pos_reverse={y:x for x,y in pos.items()}





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
            pos["d8"]: Queen(pos["d8"][0], pos["d8"][1], self.queen_img,1),
            pos["c8"]: Bishop(pos["c8"][0], pos["c8"][1], self.bishop_img,1),
            pos["f8"]: Bishop(pos["f8"][0], pos["f8"][1], self.bishop_img,1),
            pos["b8"]: Knight(pos["b8"][0], pos["b8"][1], self.knight_img,1),
            pos["g8"]: Knight(pos["g8"][0], pos["g8"][1], self.knight_img,1),
            pos["a8"]: Rook(pos["a8"][0], pos["a8"][1], self.rook_img,1),
            pos["h8"]: Rook(pos["h8"][0], pos["h8"][1], self.rook_img,1),
            pos["a7"]: Pawn(pos["a7"][0], pos["a7"][1], self.pawn_img,1),
            pos["b7"]: Pawn(pos["b7"][0], pos["b7"][1], self.pawn_img,1),
            pos["c7"]: Pawn(pos["c7"][0], pos["c7"][1], self.pawn_img,1),
            pos["d7"]: Pawn(pos["d7"][0], pos["d7"][1], self.pawn_img,1),
            pos["e7"]: Pawn(pos["e7"][0], pos["e7"][1], self.pawn_img,1),
            pos["f7"]: Pawn(pos["f7"][0], pos["f7"][1], self.pawn_img,1),
            pos["g7"]: Pawn(pos["g7"][0], pos["g7"][1], self.pawn_img,1),
            pos["h7"]: Pawn(pos["h7"][0], pos["h7"][1], self.pawn_img,1),
        }
        self.name_list = []

    def getpositin(self, xold, yold, xnew, ynew):
        self.list[(xold, yold)], move()

    def draw_pieces(self, win):
        for key, value in self.list.items():
            value.draw(win)
    
    def death(self, xpos, ypos):
        if(xpos, ypos) in self.list:
            self.list.pop((xpos, ypos))

    def manage(self, current_piece, xpos, ypos):
        self.list[(xpos,ypos)] = current_piece
        self.list.pop((current_piece.x, current_piece.y))


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
            pos["d1"]: Queen(pos["d1"][0], pos["d1"][1], self.queen_img,0),
            pos["c1"]: Bishop(pos["c1"][0], pos["c1"][1], self.bishop_img,0),
            pos["f1"]: Bishop(pos["f1"][0], pos["f1"][1], self.bishop_img,0),
            pos["b1"]: Knight(pos["b1"][0], pos["b1"][1], self.knight_img,0),
            pos["g1"]: Knight(pos["g1"][0], pos["g1"][1], self.knight_img,0),
            pos["a1"]: Rook(pos["a1"][0], pos["a1"][1], self.rook_img,0),
            pos["h1"]: Rook(pos["h1"][0], pos["h1"][1], self.rook_img,0),
            pos["a2"]: Pawn(pos["a2"][0], pos["a2"][1], self.pawn_img,0),
            pos["b2"]: Pawn(pos["b2"][0], pos["b2"][1], self.pawn_img,0),
            pos["c2"]: Pawn(pos["c2"][0], pos["c2"][1], self.pawn_img,0),
            pos["d2"]: Pawn(pos["d2"][0], pos["d2"][1], self.pawn_img,0),
            pos["e2"]: Pawn(pos["e2"][0], pos["e2"][1], self.pawn_img,0),
            pos["f2"]: Pawn(pos["f2"][0], pos["f2"][1], self.pawn_img,0),
            pos["g2"]: Pawn(pos["g2"][0], pos["g2"][1], self.pawn_img,0),
            pos["h2"]: Pawn(pos["h2"][0], pos["h2"][1], self.pawn_img,0),
        }
        self.name_list = []

    def getpositin(self, xold, yold, xnew, ynew):
        self.list[(xold, yold)], move()

    def draw_pieces(self, win):
        for key, value in self.list.items():
            value.draw(win)
    
    def manage(self, current_piece, xpos, ypos):
        self.list[(xpos,ypos)] = current_piece
        self.list.pop((current_piece.x, current_piece.y))

    def death(self, xpos, ypos):
        if(xpos, ypos) in self.list:
            self.list.pop((xpos, ypos))

class init_pieces:

    def __init__(self, turn=0):
        self.black = Black()
        self.white = White()
        self.turn = turn
        self.current_piece = None

    def draw(self, win):
        self.black.draw_pieces(win)
        self.white.draw_pieces(win)

    def __contains__(self,pos):
        if(self.turn==0):
            if((pos[0],pos[1]) in self.white.list):
                self.curr_xpos=pos[0]
                self.curr_ypos=pos[1]
                return True
        if(self.turn==1):
            if((pos[0], pos[1]) in self.black.list):
                self.curr_xpos=pos[0]
                self.curr_ypos=pos[1]
                return True
        return False

    def possible_draw(self,win):
        if self.turn == 0:
            self.current_piece = self.white.list[self.curr_xpos,self.curr_ypos]
            self.current_piece.possible_moves(win, self.black.list, self.white.list)
        if self.turn == 1:
            self.current_piece = self.black.list[self.curr_xpos,self.curr_ypos]
            self.current_piece.possible_moves(win, self.white.list, self.black.list)


    def possible_draw_remove(self,win):
        if self.current_piece:
            self.current_piece.possible_moves_remove(win)
    
    def move_piece(self,win, xpos,ypos):
        
        if (xpos,ypos) in self.current_piece.possible or (xpos,ypos) in self.current_piece.possible_kill:
            if self.turn==0:
                self.white.manage(self.current_piece, xpos, ypos)
                self.black.death(xpos, ypos)
                self.turn = 1
            else:
                self.black.manage(self.current_piece, xpos, ypos)
                self.white.death(xpos, ypos)
                self.turn = 0
            self.current_piece.move(win, xpos,ypos)
            

if __name__ == "__main__":
    board(800)
    print(pos_reverse)