from piece import piece

class Queen(piece):
    def __init__(self, x, y, image, color):
        super().__init__(image)
        self.x = x
        self.y = y
        self.possible = []
        self.color = color
        self.possible_kill = []

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
    
    def utility_check(self, xpos, ypos, opponent_list, friendly_list, change_x, change_y):
        xpos = xpos + change_x
        ypos = ypos + change_y
    
        while xpos<=800 and ypos <= 800  and xpos>=0 and ypos>=0: 
            
            if (xpos,ypos) in friendly_list:
                break
            if (xpos,ypos) not in friendly_list and (xpos,ypos) not in opponent_list:
                self.possible.append((xpos,ypos)) 
            if (xpos,ypos) in opponent_list:
                self.possible_kill.append((xpos,ypos))
                break
            xpos = xpos + change_x
            ypos = ypos + change_y
    
        

    def possible_moves(self, win, opponent_list, friendly_list):
        """Prior Moves check.
        """
        xpos=self.x
        ypos=self.y
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,100)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,-100)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,100)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,-100)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 0,100)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 0,-100)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, 100,0)
        self.utility_check(xpos, ypos, opponent_list, friendly_list, -100,0)

        super().possible_draw(win, self.possible, self.possible_kill)

    def possible_moves_remove(self, win):

        for i in self.possible:
            super().erase(win, i)
        self.possible=[]
        for i in self.possible_kill:
            super().erase(win, i)
        self.possible_kill=[]

            

    def name(self):
        return "queen"

   