import random



random_number = random.randint(1,9)

correct = False

guess_count = 0

while correct == False:
    guess = input("Guess a number between 1 and 9: ")
    if guess == 'exit' or guess == 'Exit':
        break
    if int(guess) == random_number:
        guess_count += 1
        print("You got it! You guessed the correct number in", guess_count, "guesses!")
        correct = True
    elif int(guess) > random_number:
        print("You're too high! Come back down!")
        guess_count += 1
        print("You have made: ", guess_count, "guesses.")
    elif int(guess) < random_number:
        print("You're too low! Get on up!")
        guess_count += 1
        print("You have made: ", guess_count, "guesses.")
