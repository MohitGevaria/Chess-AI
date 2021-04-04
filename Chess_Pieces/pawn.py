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

    def possible_moves(self, win, opponent_list, friendly_list):
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
        self.kill(opponent_list)    
                
        super().possible_draw(win, self.possible, self.possible_kill)

    def possible_moves_remove(self, win):
        for i in self.possible:
            super().erase(win, i)
        self.possible=[]
        for i in self.possible_kill:
            super().erase(win, i)
        self.possible_kill=[]

            

    def name(self):
        return "pawn"

    def kill(self, opponent_list):
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