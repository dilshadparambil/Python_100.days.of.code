# Turtle Racing 

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for obj in all_turtles:
        x=obj.xcor()
        if x>=230:
            is_race_on = False
            winner_colour=obj.pencolor()
            if user_bet == winner_colour:
                print("you win ")
            else:
                print(f"you lose,the winner is {winner_colour}")

        obj.forward(random.randint(0, 10))


screen.exitonclick()