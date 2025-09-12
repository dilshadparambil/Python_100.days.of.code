# Higher Lower Game 
# You need to download art.py,game_data.py from Beginner/d14 folder in order to run this file
import random
import art
from game_data import data

def get_print_data():
    selection=random.choice(data)
    return selection

def more_followers(a_count,b_count):
    if a_count>b_count:
        return 'a'
    else:
        return 'b'

def proceed(choice):
    global a,b
    if choice=='b':
        a=b
    b=get_print_data()
    while a==b:
        b=get_print_data()


def game_continue(usr_score):
    print(art.logo)
    game_over = False
    while not game_over:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

        user_input=input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)
        print(art.logo)

        if more_followers(a['follower_count'],b['follower_count'])==user_input:
            usr_score+=1
            print(f"You're right! Current score: {usr_score}")
            proceed(user_input)
        elif a['follower_count']==b['follower_count']:
            print("both have same followers")
            proceed(user_input)
        else:
            print(f"Sorry, that's wrong. Final score: {usr_score}")
            game_over=True


a=get_print_data()
b=get_print_data()
while a==b:
    b=get_print_data()
score=0
game_continue(score)