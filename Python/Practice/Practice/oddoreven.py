number = int(input("Give me a number.\n"))
if (number % 2) == 0:
    print("Even")
elif (number % 4) == 0:
    print("Multiple of 4!")
else:
    print("Odd")
    
num = int(input("Enter first number: \n"))
check = int(input("Enter second number: \n"))
if (num % check) == 0:
    print("It divides evenly!")
else:
    print("It does NOT divide evenly!")