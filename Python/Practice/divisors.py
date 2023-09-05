num = int(input("Pick a number, any number!: "))
num_range = range(1, num)
divisor = []
for i in num_range:
    if num % i == 0:
        divisor.append(i)
print("It looks like", num, "is divisable by", divisor)