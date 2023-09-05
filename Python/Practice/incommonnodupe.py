a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []
for i in a:
    if i in b:
        new_list.append(i)
for i in new_list:
    if new_list.count(i) > 1:
        new_list.remove(i)
print(new_list)