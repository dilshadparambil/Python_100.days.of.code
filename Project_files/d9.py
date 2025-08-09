# Blind Auction
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
auction={}

def highest_bidder(dict_auction):
    max_value = 0
    max_user=''
    for user_name in dict_auction:
        if dict_auction[user_name]>max_value:
            max_value=dict_auction[user_name]
            max_user=user_name

    print(f"The winner is {max_user} with a bid of ${max_value}")


flag=True
while flag:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    auction[name] = bid
    choice=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if choice=="no":
        flag=False
        highest_bidder(auction)
    else:
        print("\n" * 20)
