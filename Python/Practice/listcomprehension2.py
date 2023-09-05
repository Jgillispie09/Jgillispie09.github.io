a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# List comprehension new_list is created for comprehension. new_list = [i for i in a if i in b] - i iterates for each number(i) in a, if i is also in b it gets added to the list.
# Basically we are saying new_list consists of each instance of i passing through a and b both
# Second part, the for loop indicates that for each number(i) in new_list, if the .count() function detects more than 1 instance of the same number, it will remove the first instance of that number.
# Not the most effective way in that if I had multiple duplicates, 3 of the same number or more, I would need a new method by which to filter out the duplicate.
new_list = [i for i in a if i in b]
for i in new_list:
    if new_list.count(i) > 1:
        new_list.remove(i)
        
print(new_list)