from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Pong')

paddle_Right = Paddle((350, 0))
paddle_Left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_Right.go_up, 'Up')
screen.onkey(paddle_Right.go_down, 'Down')
screen.onkey(paddle_Left.go_up, 'w')
screen.onkey(paddle_Left.go_down, 's')

game_on = True
while game_on==True:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # bouncing from walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_walls()

    # bouncing from right paddle
    if ball.xcor() > 340 and ball.distance(paddle_Right) < 50:
        ball.bounce_paddle()

    if ball.xcor() < -340 and ball.distance(paddle_Left)<50:
        ball.bounce_paddle()

    if ball.xcor() > 390:
        ball.returning_center()
        scoreboard.update_score_Left()

    if ball.xcor() < -390:
        ball.returning_center()
        scoreboard.update_score_Right()

    if scoreboard.score_right ==10 or scoreboard.score_left==10:
        scoreboard.game_over()
        game_on = False


screen.exitonclick()
