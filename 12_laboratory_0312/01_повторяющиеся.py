lst = [4, 5, 6, 2, 3, 7, 8, 4, 9, 2, 5]
element = 0

while element < len(lst):
    for index in range(element + 1, len(lst) -1):
        if lst[index] == lst[element]:
            lst.pop(index)
    element += 1

print(lst)
