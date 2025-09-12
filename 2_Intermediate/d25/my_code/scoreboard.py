import turtle

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0

    def write_output(self,x,y,answer):
        self.score += 1
        self.goto(x,y)
        self.write(answer, align='left', font=("Arial", 8, "normal"))


    def winner(self):
        if self.score == 50:
            self.goto(0, 0)
            self.write("YOU WIN", align='center', font=("Arial", 40, "bold"))
            return True
        return False