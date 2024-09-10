from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(position)
    def go_up(self):
        y_coordinate = self.ycor()+20
        self.goto(self.xcor(), y_coordinate)
    def go_down(self):
        y_coordinate = self.ycor()-20
        self.goto(self.xcor(), y_coordinate)



