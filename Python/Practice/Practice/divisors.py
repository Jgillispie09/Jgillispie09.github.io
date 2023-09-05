num = int(input("Enter a number to find divisors: \n"))
listRange = list(range(1,num+1))
divisorList = []
for number in listRange:
    if num % number == 0:
        divisorList.append(number)
        
print(divisorList)