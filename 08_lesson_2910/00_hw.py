import random as r

r_list = []
for i in range(10):
    r_list.append(r.randint(1, 100))

print(f'список: {r_list}')

maximum = 0
for element in r_list:  # просматриваю каждый элемент списка
    if element > maximum:  # если текущий элемент больше максимума
        maximum = element  # присвоить максимуму элемент

print(f'Максимальное: {maximum}')


