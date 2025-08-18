from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.score=0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}",False,align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("yellow")
        self.write("GAME OVER!!!",align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.score+=1
        self.print_score()