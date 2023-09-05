print("Welcome to the game!")
name = input("What is your name?: ")
age = int(input("What is your age?: "))
print("Hello", name, "you are", age, "years old!")
is_older = age >= 18


if is_older == True:
    print("You are old enough to play!")
    play = input("Would you like to play?\n (y/n)?: ")
    if play == 'y' or play == 'Y':
        print("Let the games begin!")
    elif play == 'n' or play == 'N':
        print("Farewell!")
    else:
        while play == '':
            print("Please enter a valid command")
elif age >= 14 and age <= 17:
    print("Your parent must give you permission to play!")
    parent = input("Is your guardian with you?\n (y/n)?: ")
    if parent == 'y' or parent == 'Y':
        print("Please have your guardian give you permission to play!")
        permission = input("Does " + name + " have permission to play? \n (y,n)?: ")
        if permission == 'y' or permission == 'Y':
            print("Let the games begin!")
        else:
            print("Farewell!")
else:
    print("You are too young to play!")