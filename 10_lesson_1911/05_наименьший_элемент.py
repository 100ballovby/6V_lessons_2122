import random as r

r_list = []
for i in range(20):
    r_list.append(r.randint(1, 50))

print(r_list)

minimum = r_list[0]  # минимум - самый первый элемент
for element in r_list:  # просмотреть каждый элемент списка
    if element < minimum:  # если элемент меньше минимума
        minimum = element  # переписать минимум
print(f'Самый маленький элемент: {minimum}')


