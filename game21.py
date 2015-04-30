#Corey Dew
#cs21
#Question: Roll dice to play 21

import random
def main():
    user_total = 0
    cpu_total = 0
    option = input("Do you want to roll?(y, n) ")
    while option == "y"and cpu_total <= 21 and user_total <= 21:
        d1, d2 = roll_dice()
        user_total = user_total + d1 + d2
        print("user points: ", user_total)
        d1, d2 = roll_dice()
        cpu_total = cpu_total + d1 + d2
        if cpu_total <= 21 and user_total <= 21:
            option = input("Do you want to roll?(y, n) ")
        if option == "n":
            print("user points: ", user_total)
            print("cpu points: ", cpu_total)
    if user_total >= 21:
        print("cpu points: ", cpu_total)
        print("CPU WINS!!!")
    elif cpu_total >= 21:
        print("cpu points: ", cpu_total)
        print("USER WINS!!!")
    elif cpu_total > user_total:
        print("CPU WINS!!!")
    elif user_total > cpu_total:
        print("USER WINS!!!")
    elif cpu_total == user_total:
        print("Its a tie, so USER WINS!!!")
def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1, d2

main()
    
