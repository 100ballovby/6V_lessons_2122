"""
Найти сумму положительных элементов списка,
где значения - случайные числа в диапазоне
от -100 до 20. Всего в массиве 30 чисел.
"""
import random as r

r_list = []
for i in range(30):
    r_list.append(r.randint(-100, 20))

print(r_list)
summary = 0
for element in r_list:
    if element > 0:
        summary += element
print(summary)
