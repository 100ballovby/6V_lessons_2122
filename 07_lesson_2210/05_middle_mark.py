"""Задача №1. Написать программу, которая получает оценки 10 учеников
за контрольную, записывает их в список и считает среднее арифметическое.
Оценки вводятся через input(). Чтобы получить сумму оценок из списка,
нужно список обернуть в функцию sum()"""

marks = []
students = int(input('Сколько учеников? '))
for mark in range(students):
    m = int(input(f'Введите оценку {mark + 1}: '))
    marks.append(m)

summ = sum(marks)
print(f'Средний балл группы: {summ / students}.')
