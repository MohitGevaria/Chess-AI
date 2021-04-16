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
            pos["e8"]: King(pos["e8"][0], pos["e8"][1], self.king_img,1),
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
            return self.list.pop((xpos, ypos))

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
            pos["e1"]: King(pos["e1"][0], pos["e1"][1], self.king_img,0),
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

    def return_manage(self, current_piece, xpos, ypos):
        self.list[(xpos,ypos)] = current_piece
        self.list.pop((current_piece.x, current_piece.y))


    def death(self, xpos, ypos):
        if(xpos, ypos) in self.list:
            return self.list.pop((xpos, ypos))

class init_pieces:

    def __init__(self, turn=0):
        self.black = Black()
        self.white = White()
        self.turn = turn
        self.current_piece = None
        self.white_king = self.white.list[pos["e1"]]
        self.black_king = self.black.list[pos["e8"]]
        self.king_checkers = []
        self.king_checkers_2 = []
        self.deletd_piece = None
        self.enpassant = None

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

    def return_to_initial_state(self, xpos,ypos):
        
        nxpos,nypos = self.current_piece.x, self.current_piece.y
        self.current_piece.x, self.current_piece.y = xpos,ypos
        if self.turn == 0:
            self.white.list[(xpos,ypos)] = self.current_piece
            self.white.list.pop((nxpos,nypos)) 
            
            if(self.deletd_piece):
                self.black.list[(nxpos,nypos)] = self.deletd_piece 
            self.deletd_piece = None    
        else:
            self.black.list[(xpos,ypos)] = self.current_piece
            self.black.list.pop((nxpos,nypos)) 
            
            if(self.deletd_piece):
                self.white.list[(nxpos,nypos)] = self.deletd_piece 
            self.deletd_piece = None

    def validate_each_move(self):
        xold,yold = self.current_piece.x, self.current_piece.y    
        
        for each_move in self.current_piece.possible:
            
            
            self.possible_move_piece(each_move[0], each_move[1])
            self.checking_condition2(self.white.list, self.black.list)

            if len(self.king_checkers_2)!= 0:
                self.current_piece.possible=[] 
                self.return_to_initial_state(xold, yold)
                break   
            self.return_to_initial_state(xold, yold)


        for each_move in self.current_piece.possible_kill:
            
            if self.turn==1 and (each_move[0], each_move[1]) in self.white.list:
                self.deleted_piece = self.white.list[(each_move[0], each_move[0])]
            if self.turn==0 and (each_move[0], each_move[1]) in self.black.list:
                self.deleted_piece = self.black.list[(each_move[0], each_move[1])]
            
            self.possible_move_piece(each_move[0], each_move[1])
            self.checking_condition2(self.white.list, self.black.list)
            


            if len(self.king_checkers_2)!= 0:
                self.current_piece.possible_kill=[]
                self.return_to_initial_state(xold, yold)
                break
            self.return_to_initial_state(xold, yold)
    
    def validate_each_move_for_king(self): 
        
        xold,yold = self.current_piece.x, self.current_piece.y    
        
        if(len(self.current_piece.possible) != 0):
            for each_move in self.current_piece.possible:
                self.possible_move_piece(each_move[0], each_move[1])
                self.checking_condition2(self.white.list, self.black.list)

                if len(self.king_checkers_2)!= 0:
                    self.current_piece.possible.remove(each_move)    
                self.return_to_initial_state(xold, yold)
        
        if(len(self.current_piece.possible_kill)!=0):        
            for each_move in self.current_piece.possible_kill:

                if self.turn==1 and (each_move[0], each_move[1]) in self.white.list:
                    self.deleted_piece = self.white.list[(each_move[0], each_move[1])]
                if self.turn==0 and (each_move[0], each_move[1]) in self.black.list:
                    self.deleted_piece = self.black.list[(each_move[0], each_move[1])]
            
            
                self.possible_move_piece(each_move[0], each_move[1])
                self.checking_condition2(self.white.list, self.black.list)
                
                if len(self.king_checkers_2)!= 0:
                    self.current_piece.possible_kill.remove(each_move)
                self.return_to_initial_state(xold, yold)   

    def possible_draw(self,win):
        if self.turn == 0:
            self.current_piece = self.white.list[self.curr_xpos,self.curr_ypos]
            
            if len(self.king_checkers) == 0:
                
                if self.current_piece.name() == "pawn":
                        self.current_piece.possible_moves( self.black.list, self.white.list, self.black_king, self.enpassant)
                else:    
                        self.current_piece.possible_moves( self.black.list, self.white.list, self.black_king)
                

                self.validate_each_move()
                self.current_piece.possible_draw(win, self.current_piece.possible, self.current_piece.possible_kill)
            
            elif len(self.king_checkers) == 1:
                self.current_piece.on_check_move(self.king_checkers[0], self.black.list, self.white.list, self.white_king,self.black_king)
                self.king_checkers[0].possible_kill = [] 

                if self.current_piece.name() == "king":

                    self.validate_each_move_for_king()
                
                else:    

                    self.validate_each_move()
    
                self.current_piece.possible_draw(win, self.current_piece.possible, self.current_piece.possible_kill)
            
            elif len(self.king_checkers) == 2:
                if self.current_piece.name() == "king":

                    self.current_piece.on_check_move(self.king_checkers[0], self.black.list, self.white.list, self.white_king,self.black_king)
                    self.king_checkers[0].possible_kill = []     
                    self.validate_each_move_for_king()
                
                else:
                    self.current_piece.possible=[]
                    self.current_piece.possible_kill=[]
        
        if self.turn == 1:
           
            self.current_piece = self.black.list[self.curr_xpos,self.curr_ypos]
           
            if len(self.king_checkers) == 0:
            
                self.current_piece.possible_moves( self.white.list, self.black.list, self.white_king)
                self.validate_each_move()
                self.current_piece.possible_draw(win, self.current_piece.possible, self.current_piece.possible_kill)
           
            elif len(self.king_checkers) == 1:
                
                self.current_piece.on_check_move(self.king_checkers[0], self.white.list, self.black.list, self.black_king,self.white_king)
                self.king_checkers[0].possible_kill = [] 
                    
                if self.current_piece.name() == "king":
                    self.validate_each_move_for_king()
                
                else:    
                    self.validate_each_move()
        
                self.current_piece.possible_draw(win, self.current_piece.possible, self.current_piece.possible_kill)
                
            elif len(self.king_checkers) == 2:
                if self.current_piece.name() == "king":

                    self.current_piece.on_check_move(self.king_checkers[0], self.white.list, self.black.list, self.black_king,self.white_king)
                    self.king_checkers[0].possible_kill = []     
                    self.validate_each_move_for_king()
                
                else:
                    self.current_piece.possible=[]
                    self.current_piece.possible_kill=[]

    def possible_draw_remove(self,win):
        if self.current_piece:
            self.current_piece.possible_moves_remove(win)
    
    def move_piece(self,win, xpos,ypos):
        
        if (xpos,ypos) in self.current_piece.possible or (xpos,ypos) in self.current_piece.possible_kill:
            
            if(self.current_piece.name() == "pawn"):
                if(self.current_piece.initial==True):
                    self.enpassant = (xpos,ypos)
            if self.turn==0:
                self.white.manage(self.current_piece, xpos, ypos)
                self.black.death(xpos, ypos)
                self.turn = 1
            else:
                self.black.manage(self.current_piece, xpos, ypos)
                self.white.death(xpos, ypos)
                self.turn = 0
            self.current_piece.move(win, xpos,ypos)

    def possible_move_piece(self, xpos,ypos,):
        
        #if (xpos,ypos) in self.current_piece.possible or (xpos,ypos) in self.current_piece.possible_kill:
        if self.turn==0:
            self.white.manage(self.current_piece, xpos, ypos)
            self.deleted_piece = self.black.death(xpos, ypos)

        else:
            self.black.manage(self.current_piece, xpos, ypos)
            
            self.deleted_piece = self.white.death(xpos, ypos)
        
        self.current_piece.possible_move_on_check(xpos,ypos)

    def checking_condition(self):
        self.king_checkers=[]
        if self.turn==0:
            for _,i in self.black.list.items():
                i.possible_moves(self.white.list, self.black.list, self.black_king)
                if (self.white_king.x,self.white_king.y) in i.possible_kill and i not in self.king_checkers:
                    self.king_checkers.append(i)
                i.possible = []
                i.possible_kill = []        
        else:
            for _,i in self.white.list.items():
                i.possible_moves( self.black.list, self.white.list, self.white_king)
                if (self.black_king.x,self.black_king.y) in i.possible_kill and i not in self.king_checkers:
                    
                    self.king_checkers.append(i)    
                i.possible = []
                i.possible_kill = [] 

    def checking_condition2(self, white_list, black_list):
        self.king_checkers_2=[]
        if self.turn==0:
            for _,i in black_list.items():
                i.possible_moves(white_list, black_list, self.black_king)
                if (self.white_king.x,self.white_king.y) in i.possible_kill and i not in self.king_checkers_2:
                    self.king_checkers_2.append(i)
                i.possible = []
                i.possible_kill = []        
        else:
            for _,i in white_list.items():
                i.possible_moves( black_list, white_list, self.white_king)
                if (self.black_king.x,self.black_king.y) in i.possible_kill and i not in self.king_checkers_2:
                    
                    self.king_checkers_2.append(i)    
                i.possible = []
                i.possible_kill = [] 


if __name__ == "__main__":
    board(800)
    