a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for i in a:
    if i < 5:
        new_list.append(i)
print(new_list)

num = int(input("pick a number, any number.: "))
print("I'm going to give you a list of numbers which are smaller than this number.")
smaller_than_num = []
for i in a:
    if i < num:
        smaller_than_num.append(i)
print(smaller_than_num)

# First one in one line.
print([i for i in a if i < 5])