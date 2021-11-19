import random as r

r_list = []
for i in range(10):  # повторить 10 раз
    r_list.append(r.randint(1, 100))  # сгенерировать число и поместить в список

print(r_list)

summary = 0
even = []
for index in range(len(r_list)):  # повторить <длина списка> раз
    if r_list[index] % 2 == 0:
        even.append(r_list[index])
        summary += r_list[index]

print(even)
print(summary / len(even))

