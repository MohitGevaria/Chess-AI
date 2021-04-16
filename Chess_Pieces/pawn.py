from piece import piece


class Pawn(piece):
    def __init__(self, x, y, image, color):
        super().__init__(image)
        self.x = x
        self.y = y
        self.initial = True
        self.possible = []
        self.color = color
        self.possible_kill = []
        self.king_line_of_attack = []



    def draw(self, win):
        super().draw(win ,self.x, self.y)

    def move(self, win, newx, newy):
        self.erase(win,(self.x,self.y))
        self.x = newx
        self.y = newy
        self.possible_moves_remove(win)
        self.initial = False
        self.possible=[]
        self.possible_kill=[] 
        self.draw(win) 
    
    def utility_check(self, xpos, ypos, opponent_list, friendly_list):
        if ((xpos,ypos) not in opponent_list) and ((xpos,ypos) not in friendly_list):
            self.possible.append((xpos,ypos))
            return True
        return False

    def possible_moves(self, opponent_list, friendly_list, opponent_king, enpassant=None):
        xpos=self.x
        ypos=self.y
        if self.initial:
            if self.color:
                if self.utility_check(xpos,ypos+100,opponent_list,friendly_list):
                    self.utility_check(xpos,ypos+200,opponent_list,friendly_list)

            else:
                if self.utility_check(xpos,ypos-100,opponent_list,friendly_list):
                    self.utility_check(xpos,ypos-200,opponent_list,friendly_list)

            
        else:
            
            if self.color:
                if(self.end_of_board(xpos,ypos+100)):
                    self.utility_check(xpos,ypos+100,opponent_list,friendly_list)
            else:
                if(self.end_of_board(xpos,ypos-100)):
                    self.utility_check(xpos,ypos-100, opponent_list, friendly_list)



        self.kill(opponent_list, enpassant)    
                
        #super().possible_draw(win, self.possible, self.possible_kill)

    def possible_moves_remove(self, win):
        for i in self.possible:
            super().erase(win, i)
        self.possible=[]
        for i in self.possible_kill:
            super().erase(win, i)
        self.possible_kill=[]

    def possible_move_on_check(self, newx, newy):
        """
        posterior move.
        """
        self.x = newx
        self.y = newy
        
    def on_check_move(self, king_checkers ,opponent_list,friendly_list, friendly_king,opponent_king):
        king_checkers.possible_moves( friendly_list, opponent_list, friendly_king)
        temp= []
        temp_kill=[]
        king_checkers_possible = king_checkers.king_line_of_attack
        self.possible_moves(opponent_list,friendly_list, opponent_king)
        for i in self.possible:
            if i in king_checkers_possible:
                temp.append(i)
 
        if (king_checkers.x,king_checkers.y) in self.possible_kill:
           
            temp_kill.append((king_checkers.x,king_checkers.y))

        self.possible=temp
        self.possible_kill=temp_kill
        
        

    def name(self):
        return "pawn"

    def kill(self, opponent_list, enpassant=None):
        if(self.color==0):

        

            if (self.end_of_board(self.x-100, self.y-100)) and (self.x-100, self.y-100) in opponent_list:
                self.possible_kill.append((self.x-100, self.y-100))
                
            if (self.end_of_board(self.x+100, self.y-100)) and (self.x+100, self.y-100) in opponent_list:
                self.possible_kill.append((self.x+100, self.y-100))
        else:    
            if (self.end_of_board(self.x+100, self.y+100)) and (self.x+100, self.y+100) in opponent_list:
                self.possible_kill.append((self.x+100, self.y+100))
            if (self.end_of_board(self.x-100, self.y+100)) and (self.x-100, self.y+100) in opponent_list:
                self.possible_kill.append((self.x-100, self.y+100))