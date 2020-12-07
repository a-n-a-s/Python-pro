import random


def rollDice():
    number = random.randint(1, 6)
    if (number == 1):
        print("You got :", number)
    elif (number == 2):
        print("You got :", number)
    elif (number == 3):
        print("You got :", number)
    elif (number == 4):
        print("You got :", number)
    elif (number == 5):
        print("You got :", number)
    else:
        print("you Got :", number)

    x = input("(Do You Want To Try Again(Y)")
    x.lower()
    if (x == "y"):
        rollDice()


rollDice()
