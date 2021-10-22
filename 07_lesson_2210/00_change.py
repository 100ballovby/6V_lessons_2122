a = 3 + 6
b = 11

tmp = a  # 9
a = b   # 11
b = tmp  # 9
print(f'a = {a}')
print(f'b = {b}')

a, b = b, a
print(f'a = {a}')
print(f'b = {b}')
