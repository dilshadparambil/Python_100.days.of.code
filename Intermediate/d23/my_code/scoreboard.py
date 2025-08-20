from turtle import Turtle
import player

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_count=0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-270,270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"LEVEL:{self.level_count}", align="left", font=FONT)

    def update_level(self):
        self.level_count+=1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)