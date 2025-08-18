# Snake Game P2
# You need to download snake.py, food.py, scoreboard.py from Intermediate/d21/my_code folder in order to run this file
from turtle import Screen
from score import Score
from snake import Snake
from food import Food
import time

scr=Screen()
scr.setup(height=600,width=600)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.tracer(0)

snake=Snake()
food=Food()
score=Score()

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

    if snake.head.distance(food)<=15:
        food.spawn_food()
        snake.grow_snake()
        score.update_score()


    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-290 or snake.head.ycor()<-280:
        score.game_over()
        game_on=False

    for part in snake.snake_body[1:]:
        if snake.head.distance(part)<10:
                score.game_over()
                game_on = False


scr.exitonclick()