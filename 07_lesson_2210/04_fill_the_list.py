"""Наполнить список 10 случайными числами"""
import random as r

r_list = []  # пустой список
for number in range(10):  # повторить 10 раз
    n = r.randint(1, 1000)  # сгенерировать случайное число в диапазоне от 1 до 1000
    r_list.append(n)  # добавить случайное число в список

print(f'Список случайных чисел: {r_list}.')

"""Задача №1. Написать программу, которая получает оценки 10 учеников 
за контрольную, записывает их в список и считает среднее арифметическое. 
Оценки вводятся через input(). Чтобы получить сумму оценок из списка,
нужно список обернуть в функцию sum()"""
