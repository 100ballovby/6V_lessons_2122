def say_hello():  # определение функции
    # тело функции
    txt = 'Hello, world!'
    return txt  # возвращает строку из переменной txt

# чтобы функция работала, ее нужно вызвать по имени
greet = say_hello()  # вызов функции

print(greet)
print(greet[5])  # достаю 5 символ из возвращенного результата работы функции

