import random


def new_funct():
    random_ran = random.randint(1,100)
    while True:
        a = int(input('Enter your guess: '))
        if a == random_ran:
            print("You have matched Correct!")
            break
        elif a < random_ran:
            print("Too Low")
        else:
            print("Too High")

new_funct()
