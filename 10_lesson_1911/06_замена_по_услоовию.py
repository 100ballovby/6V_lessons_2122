my_list = [1, 6, 0, 12, 6, 0, 4, 3, 0, 0, 1]
# заменить все 0 на None
for index in range(len(my_list)):
    if my_list[index] == 0:  # если элемент с определенным индексом равен 0
        my_list[index] = None  # заменить элемент с этим индексом на None

print(my_list)



