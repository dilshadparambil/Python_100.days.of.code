from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x=10
        self.y=10
        self.speed_time=0.1

    def ball_move(self):
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x,new_y)

    def ball_reset(self):
        self.goto(0,0)
        self.speed_time = 0.1
        self.change_direction_up()

    def change_direction_down(self):
        self.y *= -1

    def change_direction_up(self):
        self.x *= -1
        self.speed_time*=0.9