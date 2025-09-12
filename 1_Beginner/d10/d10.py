# Calculator
# You need to download art.py from Beginner/d10 folder in order to run this file
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    flag=True
    num1 = float(input("What's the first number?: "))

    while flag:

        for symbol in calc:
            print(symbol)

        op = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        res = calc[op](num1, num2)
        print(f"{num1} {op} {num2} = {res}")
        calc_continue = input(
            f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation:").lower()

        if calc_continue=='y':
            num1=res
        else:
            flag=False
            calculator()

calculator()
