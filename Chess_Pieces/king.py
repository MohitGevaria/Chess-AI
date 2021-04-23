from piece import piece

class King(piece):
    def __init__(self, x, y, image, color):
        super().__init__(image)
        self.x = x
        self.y = y
        self.possible = []
        self.color = color
        self.possible_kill = []
        self.king_line_of_attack = []
        self.is_moved = False
        self.castle = {}

    # draws the piece on the board
    def draw(self, win):
        super().draw(win ,self.x, self.y)


    def move(self, win, newx, newy):
        """
        posterior move.
        """
        self.erase(win,(self.x,self.y))
        self.x = newx
        self.y = newy
        self.possible_moves_remove(win)
        self.initial = False
        self.possible=[]
        self.possible_kill=[] 
        self.draw(win) 
        
        
        self.castle = {}
    
    def utility_check(self, xpos, ypos, opponent_list, friendly_list, change_x, change_y, opponent_king):
        xpos = xpos + change_x
        ypos = ypos + change_y
        temp = []
        if xpos<=800 and ypos <= 800  and xpos>=0 and ypos>=0: 
            
            
            if (xpos,ypos) not in friendly_list and (xpos,ypos) not in opponent_list:
                self.possible.append((xpos,ypos)) 

            if (xpos,ypos) in opponent_list:
                self.possible_kill.append((xpos,ypos))
            if(xpos == opponent_king.x)and (ypos == opponent_king.y):
                self.king_line_of_attack.append((xpos,ypos))
                self.possible_kill.remove((xpos,ypos))


            xpos = xpos + change_x
            ypos = ypos + change_y
        

    def possible_moves(self, opponent_list, friendly_list, opponent_king):
        """Prior Moves check.
        """
        xpos=self.x
        ypos=self.y
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 0,100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,0, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,0, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 0,-100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,-100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,-100, opponent_king)

        # self.castle_condition(friendly_list, opponent_list)

    def possible_moves_remove(self, win):

        for i in self.possible:
            super().erase(win, i)
        self.possible=[]
        for i in self.possible_kill:
            super().erase(win, i)
        self.possible_kill=[]

    def check_before_castle(self, friendly_list, opponent_list,  change):
        xpos = self.x + change
       
        while((xpos<750) and (xpos>50)):
            if ((xpos, self.y) in friendly_list) or ((xpos, self.y) in opponent_list): 
                return False
            xpos += change
        return True


    def castle_condition(self, friendly_list, opponent_list):
        
        if (not (self.is_moved)):
            
            if ((50,self.y) in friendly_list): 
                if (friendly_list[(50,self.y)].name() == "rook" and friendly_list[(50,self.y)].color == self.color ): 
                
                    if not (friendly_list[(50,self.y)].is_moved): #a1
                        if(self.check_before_castle(friendly_list, opponent_list, -100)):
                            self.possible.append((self.x-200,self.y))
                            self.castle[(self.x-200,self.y)] = (50,self.y)
            
            if ((750,self.y) in friendly_list):
                if (friendly_list[(750,self.y)].name() == "rook" and friendly_list[(750,self.y)].color == self.color):
                        
                    if not (friendly_list[(750,self.y)].is_moved): #h1
                        if(self.check_before_castle(friendly_list, opponent_list, +100)):
                            self.possible.append((self.x+200,self.y))
                            self.castle[(self.x+200,self.y)] = (750,self.y)
                
            
    def on_check_move(self, king_checkers ,opponent_list,friendly_list, friendly_king,opponent_king):
        

        king_checkers.possible_moves( friendly_list, opponent_list, friendly_king)
        king_checkers_possible = king_checkers.king_line_of_attack
        self.possible_moves(opponent_list,friendly_list, opponent_king)
        for i in self.possible:
            if i in king_checkers_possible:
                self.possible.remove(i)

        

    def possible_move_on_check(self, newx, newy):
        """
        posterior move.
        """
        self.x = newx
        self.y = newy
        
    
    def name(self):
        return "king"

   