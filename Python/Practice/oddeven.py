print("Ever wonder if your number is odd or even?")
print("Look no further, here is the odd/even number checkerator!")
number = int(input("Pick a number, any number!: "))
if number % 2 == 0 and number % 4 != 0:
    print("Nice, an even number!")
elif number % 4 == 0:
    print("That's a multiple of 4, oh and even!")
else:
    print("Looks a bit odd.")
print("Let's try something else now.")
num = int(input("Pick a number, any number!: "))
check = int(input("Pick a number to divide it by, let's see if it divides evenly.: "))
if num % check == 0:
    print("It's an even divide!")
else:
    print("This doesn't divide evenly, now does it?")