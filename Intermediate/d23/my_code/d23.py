# Turtle Crossing game
# You need to download cars.py, player.py, scoreboard.py from Intermediate/d23/my_code folder in order to run this file

from turtle import Screen
import time
import player
import cars
import random
from scoreboard import ScoreBoard

scr=Screen()
scr.setup(height=600,width=600)
scr.tracer(0)

timmy=player.Player()
cars=cars.Cars()
score=ScoreBoard()

scr.listen()
scr.onkey(timmy.move_turtle,"Up")

count=0
game_over=False
while not game_over:
    scr.update()
    time.sleep(0.1)
    if random.randint(1,6)==3:
        cars.car_spawn()

    for car in cars.car_list:
        if timmy.distance(car) < 20:
            score.game_over()
            game_over=True

    cars.car_move()


    if timmy.ycor() >= player.FINISH:
        score.update_level()
        timmy.player_start()
        cars.increase_speed()

scr.exitonclick()
