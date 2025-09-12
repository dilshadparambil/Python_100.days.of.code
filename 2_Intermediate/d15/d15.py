# Coffee Machine Project 

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0

def check_resources(choice):
    for key, value in MENU[choice]["ingredients"].items():
        if resources[key]<value:
            print(f"Sorry there is not enough {key}.")
            return False
    else:
        return True

def transaction_success(usr_money,choice):
    global money

    if usr_money>=MENU[choice]["cost"]:
        change=usr_money-MENU[choice]["cost"]
        if change>0:
            print(f"Here is ${change:.2f} dollars in change.")
        money+=MENU[choice]["cost"]
        return True

    else:
        print(" Sorry that's not enough money. Money refunded.")
        return False

def get_money():
    print("Please insert coinss.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def update_resources(choice):
    for key, value in MENU[choice]["ingredients"].items():
        resources[key]-=value


def coffee():

    user_choice=input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice=='off':
        exit(0)

    elif user_choice=='report':
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}\n")

    elif user_choice=='espresso' or user_choice=="latte" or user_choice=="cappuccino":
        if check_resources(user_choice):

            user_money=get_money()

            if transaction_success(user_money,user_choice):
                update_resources(user_choice)
                print(f"Here is your {user_choice} ☕️. Enjoy!")

    else:
        print("wrong choice! try again")

    coffee()

coffee()

























