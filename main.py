from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()

screen.onkey(r_paddle.goUp,"Up")
screen.onkey(r_paddle.goDown,"Down")

screen.onkey(l_paddle.goUp,"w")
screen.onkey(l_paddle.goDown,"s")

ball = Ball()

score_board = ScoreBoard()

game_is_on =True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -270 :
        ball.bounceY()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounceX()

    if ball.xcor() > 380:
        ball.resetPosition()
        score_board.lSocredPoint()

    if ball.xcor() < -380:
        ball.resetPosition()
        score_board.rSocredPoint()

screen.exitonclick()