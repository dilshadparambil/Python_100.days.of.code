import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(chosen,who):
    choice=random.choice(cards)
    if choice==11 and sum(chosen[who])>21:
        chosen[who].append(1)
    else:
        chosen[who].append(random.choice(cards))


def first_deck(chosen):
    for i in range(2):
        draw_card(chosen, 'user')
        draw_card(chosen, 'computer')


def winner():
    print(f"Your final hand: {chosen_cards["user"]}, final score: {user_score}")
    print(f"Computer's final hand: {chosen_cards["computer"]}, final score: {computer_score}")
    if computer_score==21:
        print("You lose 😃")
    elif user_score==21:
        print("You win 😃")
    elif user_score < 21:
        if user_score > computer_score:
            print("You win 😃")
        elif computer_score > 21:
            print("Opponent went over. You win 😁")
        elif user_score == computer_score:
            print("draw")
        else:
            print("You lose 😃")
    else:
        print("You lose 😃")


flag=True

while flag:
    game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_choice=='y':
        print("\n"*20)
        print(art.logo)
        flag1 = True
        chosen_cards = {
            "user": [],
            "computer": []
        }
        first_deck(chosen_cards)
        user_score = sum(chosen_cards['user'])
        computer_score = sum(chosen_cards['computer'])

        if computer_score>=21 or user_score>=21:
            winner()

        else:
            print(f"Your cards: {chosen_cards["user"]}, current score: {user_score}")
            print(f"Computer's first card: {chosen_cards["computer"][1]}")

            flag1=True

            while flag1:
                card_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if card_choice=='y':
                    draw_card(chosen_cards,'user')
                    user_score = sum(chosen_cards['user'])
                    print(f"Your cards: {chosen_cards["user"]}, current score: {user_score}")
                    print(f"Computer's first card: {chosen_cards["computer"][0]}")
                    if user_score>=21:
                        winner()
                        flag1 = False
                elif card_choice=='n':
                    while computer_score < 16:
                        draw_card(chosen_cards, 'computer')
                    winner()
                    flag1 = False

    else:
        flag=False