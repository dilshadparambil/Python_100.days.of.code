from pty import spawn
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        self.goto( x=random.randint(-280, 280) ,  y=random.randint(-280, 280) )
