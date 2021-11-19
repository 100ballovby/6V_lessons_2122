import random as r

r_list = []
for i in range(10):  # повторить 10 раз
    r_list.append(r.randint(1, 100))  # сгенерировать число и поместить в список

print(r_list)

# перебор по значению
for element in r_list:  # для каждого элемента в списке
    print(element, end=', ')
# end - это то, чем заканчивается функция print. По умолчанию там \n (новая строка)
