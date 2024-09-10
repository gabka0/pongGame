from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.write(f"{self.score_left} : {self.score_right} ", align='CENTER', font=('Courier', 30, 'normal'))

    def update_score_Left(self):
        self.clear()
        self.score_left += 1
        self.write(f"{self.score_left} : {self.score_right} ", align='CENTER', font=('Courier', 30, 'normal'))

    def update_score_Right(self):
        self.clear()
        self.score_right += 1
        self.write(f"{self.score_left} : {self.score_right} ", align='CENTER', font=('Courier', 30, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align='CENTER', font=('Courier', 30, 'normal'))
