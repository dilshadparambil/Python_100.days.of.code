from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
flag=True

while flag:

    user_choice=input(f"What would you like? {menu.get_items()}:")
    
    if user_choice == 'off':
        flag=False

    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        if menu.find_drink(user_choice):
            drink=menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)