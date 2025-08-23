# U.S. States Game  
# You need to download all files from Intermediate/d25/my_code

import turtle
import pandas
from scoreboard import ScoreBoard

scr=turtle.Screen()
score=ScoreBoard()

scr.title("States correct")
scr.addshape("./blank_states_img.gif")
turtle.shape("./blank_states_img.gif")

states_data=pandas.read_csv("./50_states.csv")

state_list=states_data['state'].to_list()
answer_list=[]
unknown_list=[]

answer = scr.textinput("Guess the state", "Whats Another States Name?").title()

game_finish=False
while not game_finish:

    if answer=="Exit":
        break

    if answer in state_list and answer not in answer_list:

        answer_list.append(answer)

        answer_state = states_data[states_data['state'] == answer]
        x=answer_state.x.item()
        y=answer_state.y.item()

        score.write_output(x,y,answer)

        game_finish = score.winner()
        if game_finish:
            break

    answer = scr.textinput(f"{score.score}/50 States Correct", "Whats Another States Name?").title()

for states in state_list:
    if states not in answer_list:
        unknown_list.append(states)

save_file=pandas.DataFrame(unknown_list)
save_file.to_csv("./unknown states.csv")


scr.exitonclick()