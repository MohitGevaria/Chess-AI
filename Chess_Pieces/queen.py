from piece import piece
import copy

class Queen(piece):

    def __init__(self, x, y, image, color):
        super().__init__(image)
        self.x = x
        self.y = y
        self.possible = []
        self.color = color
        self.possible_kill = []
        self.king_line_of_attack = []

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
    
    def possible_move_on_check(self, newx, newy):
        """
        posterior move.
        """
        self.x = newx
        self.y = newy
        
    def utility_check(self, xpos, ypos, opponent_list, friendly_list, change_x, change_y, opponent_king):
        xpos = xpos + change_x
        ypos = ypos + change_y
        temp = []
        while xpos<=800 and ypos <= 800  and xpos>=0 and ypos>=0: 
            
            if (xpos,ypos) in friendly_list:
                break
            if (xpos,ypos) not in friendly_list and (xpos,ypos) not in opponent_list:
                self.possible.append((xpos,ypos))
                temp.append((xpos,ypos))  
            if (xpos == opponent_king.x)and (ypos == opponent_king.y):
                self.king_line_of_attack = temp
            if (xpos,ypos) in opponent_list:
                self.possible_kill.append((xpos,ypos))
                break
            
            
            xpos = xpos + change_x
            ypos = ypos + change_y

    def possible_moves(self, opponent_list, friendly_list, opponent_king):
        """Prior Moves check.
        """
        xpos=self.x
        ypos=self.y
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,-100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,-100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 0,100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 0,-100, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,0, opponent_king)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,0, opponent_king)

    def possible_moves_remove(self, win):

        for i in self.possible:
            super().erase(win, i)
        self.possible=[]
        for i in self.possible_kill:
            super().erase(win, i)
        self.possible_kill=[]

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
        return "queen"

   