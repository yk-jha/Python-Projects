import random

NUM = random.randint(1 , 50)
attempts = 0
while True:
    GNUM = int(input("GUESS THE NUMBER:"))
    if(GNUM == NUM):
        print("YOU GUESSED CORRECT NUMBER IN ",attempts," attempts")
        break
    if(GNUM > NUM):
        print("YOU HAVE GUESSED THE LARGE NUMBER")
        attempts += 1
    else:
        print("YOU HAVE GUESSED THE SMALLER NUMBER")
        attempts += 1
