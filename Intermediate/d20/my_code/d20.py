# Snake Game P1
# You need to download snake.py from Intermediate/d20/my_code folder in order to run this file

from turtle import Screen
from snake import Snake
import time
scr=Screen()
scr.setup(height=600,width=600)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.tracer(0)

snake=Snake()

scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.right,"Right")
scr.onkey(snake.left,"Left")

game_on=True
while game_on:
    scr.update()
    time.sleep(0.15)

    snake.move()














scr.exitonclick()