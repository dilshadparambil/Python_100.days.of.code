import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list=[rock,paper,scissors]

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input>=3 or user_input<0:
    print("invalid input")
    exit(0)
computer_hand=random.choice(choice_list)
user_hand=choice_list[user_input]
print(user_hand)
print(f"Computer chose: {computer_hand}")

if user_hand==computer_hand:
    print("draw")
elif user_hand==rock and computer_hand==paper:
    print("you lose")
elif user_hand==rock and computer_hand==scissors:
    print("you win")
elif user_hand==scissors and computer_hand==rock:
    print("you lose")
elif user_hand==scissors and computer_hand==paper:
    print("you win")
elif user_hand==paper and computer_hand==scissors:
    print("you lose")
elif user_hand==paper and computer_hand==rock:
    print("you win")

