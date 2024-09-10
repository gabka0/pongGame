from turtle import Turtle
speed1= 10
speed2 = 10
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('white')
        self.penup()
        self.ball_speed = 0.1

    def move(self):
        x_coordinate = self.xcor() + speed1
        y_coordinate = self.ycor() + speed2
        self.goto(x_coordinate, y_coordinate)

    def bounce_walls(self):
        global speed2
        speed2 = - speed2

    def bounce_paddle(self):
        global speed1, speed2
        speed1 = -speed1
        self.ball_speed *= 0.7

    def returning_center(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_paddle()


