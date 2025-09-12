from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_SPEED = 5
SPEED_INCREASE = 10

class Cars:
    def __init__(self):
        self.car_list=[]

    def car_spawn(self):
        new_car=Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randrange(-250, 250))
        self.car_list.append(new_car)

    def car_move(self):
        for car in self.car_list:
            car.backward(START_SPEED)

    def increase_speed(self):
        global START_SPEED
        START_SPEED+=SPEED_INCREASE
