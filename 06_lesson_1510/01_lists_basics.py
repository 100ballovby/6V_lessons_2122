numbers = [3, 14, 2, 6, -6, 15, 8, 3]
print(f'Мой список: {numbers}.')
numbers.append(-99)
print(f'Мой список: {numbers}.')

numbers.insert(3, 'я вставлен')  # insert(index, elem)  вставляет в список elem на индекс index. остальные элемент сдвигаются вправо
print(f'Мой список: {numbers}.')

numbers.pop(3)
numbers.pop()
print(f'Мой список: {numbers}.')

numbers.sort()
print(f'Мой список: {numbers}.')