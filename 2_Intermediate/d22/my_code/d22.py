# Pong game
# You need to download ball.py, paddle.py, score.py from Intermediate/d22/my_code folder in order to run this file

from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

scr=Screen()
scr.bgcolor("black")
scr.setup(height=600,width=800)
scr.title("PONG")
scr.tracer(0)


paddle1=Paddle((350,0))
paddle2=Paddle((-360,0))
ball=Ball()
score1=Score((-40,250))
score2=Score((40,250))

scr.listen()
scr.onkey(paddle1.up,"Up")
scr.onkey(paddle1.down,"Down")
scr.onkey(paddle2.up,"w")
scr.onkey(paddle2.down,"s")

game_over=False
while not game_over:
    scr.update()
    time.sleep(ball.speed_time)
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.change_direction_down()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 and ball.x>0 or ball.distance(paddle2) < 50 and ball.xcor() < -330 and ball.x<0:
        ball.change_direction_up()

    if ball.xcor()>380 :
        score1.increase_score()
        ball.ball_reset()

    if ball.xcor()<-390:
        score2.increase_score()
        ball.ball_reset()



scr.exitonclick()
