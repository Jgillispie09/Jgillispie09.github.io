a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessFnums = [] #Empty List
lessNnums = [] #Empty List
for x in a: #Sets variable x for any item in a that fits filter
    if x < 5: #Selects only numbers in list lower than 5
        lessFnums.append(x) #Adds numbers from list a to new list
        lessFnums.sort() #Sorts list
print(lessFnums) #Prints list
print() #Blank Line

num = int(input("Enter a number: \n")) #Input for user
for y in a: #Sets Y as variable for itmes in a that fit filter
    if y < num: #Selects numbers less than integer 'num'
        lessNnums.append(y) #Adds number to new list
        lessNnums.sort() #Sorts new list
print(lessNnums) #Prints