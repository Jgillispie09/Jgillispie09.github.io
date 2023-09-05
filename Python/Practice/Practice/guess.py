import random
def reset():
    input("Would you like to play again?\n Y or N?\n")
    if "y" or "Y":
        guessing(random.randint(1,9))
    elif "n" or "N":
        print("Exiting Program")

def guessing(rando):
    guess = input("Pick a number between 1 and 9: ")
    while guess == rando:
        print("Correct!")
        break
    while guess != rando:
        print("Incorrect! It was", rando)
        reset()

guessing(random.randint(1,9))

#They wrote this as a while loop. Might want to go back and fix.