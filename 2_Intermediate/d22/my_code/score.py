from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")

class Score(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score=0
        self.goto(pos)
        self.score_board()

    def score_board(self):
        self.write(f"{self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_board()