import random as r

r_list = []
for i in range(10):  # повторить 10 раз
    r_list.append(r.randint(1, 100))  # сгенерировать число и поместить в список

print(r_list)
print(f'Первый элемент списка: {r_list[0]}')

for index in range(len(r_list)):  # повторить <длина списка> раз
    """Перебираю все числа от 0 до длины списка. То есть все индексы"""
    print(r_list[index], end=', ')  # вывести элемент с порядковым номером index

