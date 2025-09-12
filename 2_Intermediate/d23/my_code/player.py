from turtle import Turtle

START=(0,-280)
FINISH=280
MOVE_SPEED=5

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.player_start()

    def player_start(self):
        self.goto(START)

    def move_turtle(self):
        self.forward(MOVE_SPEED)

