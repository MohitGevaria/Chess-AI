from piece import piece

class King(piece):
    def __init__(self, x, y, image):
        super().__init__(image)
        self.x = x
        self.y = y

    def draw(self, win):
        super().draw(win, self.x, self.y)

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def name(self):
        return "king"