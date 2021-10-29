"""Найти сумму всех чисел от 1 до 50"""
summary = 0
for num in range(1, 51):  # 1 2 3 4 5 6 7.....
    summary += num

print(f'Сумма: {summary}')
