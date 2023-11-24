class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw_square(self, square):
        square.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw_rectangle(self, rectangle):
        rectangle.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color
