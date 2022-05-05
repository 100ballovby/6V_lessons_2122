"""1. Напишите функцию, которая получает строчку через аргумент и
возвращает количество символов в этой строке."""


def string_length(string):
    return len(string)


print(string_length('Привет'))

"""2. Напишите функцию, которая получает строчку и символ через 
аргументы и проверяет, есть ли заданный символ в строке."""


def check_symbol(string, symbol):
    return symbol in string


print(check_symbol('семья', 'я'))

"""3*. Напишите функцию, которая получает строчку через аргумент и 
возвращает количество символов в этой строке БЕЗ ПРОБЕЛОВ"""


def count_letters(string):
    sum = 0
    for symbol in range(len(string)):
        if string[symbol] != ' ':
            sum += 1
    return sum


print(count_letters('хорошее блюдо'))

