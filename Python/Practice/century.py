print("Hello there. Time is but a fleeting melody in the symphony that is the universe.")
name = input("What is your name?: ")
age = int(input("How old are you?: "))
print("Hello", name, "I see you are", str(age), "years old.")
permission = input("Would you like to know when you will turn 100 years old?\n(y/n)?: ")
if permission == 'y' or permission == 'Y':
    century = 100 - age
    print("Excellent, you will turn 100 in", century, "years!")
elif permission == 'n' or permission == 'N':
    print("Goodbye")
else:
    print("Command not recognized, please restart.")
current_year = 2023
know_year = input("Would you like to know the exact year?\n(y/n)?: ")
if know_year == 'y' or know_year == 'Y':
    century_year = current_year + century
    print("You will turn 100 years old in", century, "years, in the year" + str(century_year) + ".")
elif know_year == 'n' or know_year == 'N':
    print("Come back if you want to know!")
else:
    print("Command not recognized, please restart.")