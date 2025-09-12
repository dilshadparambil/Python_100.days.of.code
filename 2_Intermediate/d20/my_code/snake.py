
from turtle import Turtle
from venv import create

POS_LIST=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):
        for pos in POS_LIST:
            snake_body = Turtle(shape="square")
            snake_body.penup()
            snake_body.color("white")
            snake_body.setposition(pos)
            self.snake.append(snake_body)

    def move(self):
        for body_count in range(len(self.snake) - 1, 0, -1):
            x = self.snake[body_count - 1].xcor()
            y = self.snake[body_count - 1].ycor()
            self.snake[body_count].setposition(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)