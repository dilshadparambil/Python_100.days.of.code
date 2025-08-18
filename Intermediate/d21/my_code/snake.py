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
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]

    def create_snake(self):
        for pos in POS_LIST:
            self.add_snake_body(pos)

    def add_snake_body(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.setposition(position)
        self.snake_body.append(snake)

    def grow_snake(self):
        self.add_snake_body(self.snake_body[-1].position())


    def move(self):
        for body_count in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[body_count - 1].xcor()
            y = self.snake_body[body_count - 1].ycor()
            self.snake_body[body_count].setposition(x, y)
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