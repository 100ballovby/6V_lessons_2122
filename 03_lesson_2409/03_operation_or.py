"""Мне нужно написать программу, котоорая
получает 2 числа. И проверяются, делятся ли
хотя бы одно из этих чисел на 2 без остатка"""

num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))

if (num1 % 2 == 0) or (num2 % 2 == 0):  # если числа без остатка делятся на 2
    print('Одно число (или оба) делятся на 2 без остатка')  # сказать об этом
else:  # если одно из чисел или оба не делятся на 6
    print('Ни одно из чисел не делится на 2 без остатка')  # сказать об этом

