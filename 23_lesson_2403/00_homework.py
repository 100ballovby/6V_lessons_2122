import random as r

colors = []
alphabet = '0123456789abcdef'

for color in range(50):
    col = '#'
    for symbol in range(6):
        col += r.choice(alphabet)
    colors.append(col)

print(colors)


