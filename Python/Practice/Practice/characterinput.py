name = input("What is your name?\n")
age = int(input(name + ", how old are you?\n"))
year = 100 - age + 2023
print(name + ", you will be 100 years old in the year " + str(year) + ".")
repeat = int(input("How many copies would you like?\n"))
print(repeat * str(name + ", you will be 100 years old in the year " + str(year) + ".\n"))