import random as r
'''Task 0. Сгенерировать список рандомных чисел от
-100 до 100 и вывести все положительные элементы '''
r_list = []
for i in range(50):
    r_list.append(r.randint(-100, 100))
for elem in r_list:
    if elem > 0:
        print(elem, end=', ')
print('\n\n\n')
'''Task 1. Сгенерировать список рандомных чисел от 
-1000 до 1000 и вывести элементы, которые больше 
среднего арифметического'''
r_list2 = []
for i in range(50):
    r_list2.append(r.randint(-1000, 1000))

mid = sum(r_list2) / len(r_list2)
for elem in r_list2:
    if elem > mid:
        print(elem, end=', ')
print('\n\n\n')
'''Task 2. Сгенерировать список рандомных чисел от 
-100 до 100 и вывести сумму всех положительных элементов
 массива, которые делятся на 2, но не делятся 10'''
for elem in r_list:
    if (elem > 0) and (elem % 2 == 0) and (elem % 10 != 0):
        print(elem, end=', ')
print('\n\n\n')


'''Task 3. Сформировать шписок В из положительных элементов
шписка А, имеющих 🔥четный индекс🔥'''
new_list = []
for index in range(len(r_list)):  # 0...<длина списка>(49)
    if r_list[index] > 0 and index % 2 == 0:
        new_list.append(r_list[index])
print(new_list, end=', ')
print('\n\n\n')

new_list = []
for index in range(0, len(r_list), 2):  # 0...<длина списка>(49)
    if r_list[index] > 0:
        new_list.append(r_list[index])
print(new_list, end=', ')

'''Task 4. Найти максимальный по модулю элемент массива. =)))'''
# abs() - функция, которая берет модуль числа  из






