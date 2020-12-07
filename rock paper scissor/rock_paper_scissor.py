import random

random_number = random.randint(1, 3)

user_choice = input("Press (r) for Rock , (s) for Scissors , (p) for Paper :")
user_choice.lower()

if (random_number == 1):
    computer_choice = "r"
elif(random_number == 2):
    computer_choice = "s"
else:
    computer_choice = "p"

if(computer_choice == "r" and user_choice == "s"):
    print(
        f"You lost ! Computer has choosen : {computer_choice} and you choosed :{user_choice}")
elif(computer_choice == "r" and user_choice == "p"):
    print(
        f"You Won ! Computer has choosen :  {computer_choice} and you choosed : {user_choice}")
elif(computer_choice == "s" and user_choice == "r"):
    print(
        f"You Won ! Computer has choosen :  {computer_choice} and you choosed : {user_choice}")
elif(computer_choice == "s" and user_choice == "p"):
    print(
        f"You Lose ! Computer has choosen : {computer_choice} and you choosed :{user_choice}")
elif(computer_choice == "p" and user_choice == "r"):
    print(
        f"You Won ! Computer has choosen : {computer_choice} and you choosed :{user_choice}")
else:
    print(
        f"Draw! computer had choosen :{computer_choice} snd you had choosen :{user_choice}")
