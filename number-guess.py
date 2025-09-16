import random # import random package 


def new_funct(): 
    random_ran = random.randint(1,100) # It randomly selects number from 1 to 100
    while True: # Keeps excuting untill specific condition is True
        a = int(input('Enter your guess: '))
        if a == random_ran:
            print("You have matched Correct!")
            break
        elif a < random_ran:
            print("Too Low")
        else:
            print("Too High")

new_funct()

