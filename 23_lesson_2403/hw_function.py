def make_colors_list(count, mode='hex'):
    """
    Функция создает список кодов цветов,
    в палитре RGB или HEX.
    :param count: количество цветов в списке
    :paaram mod: модификатор кода цвета - RGB или HEX
    :return: list: список цветов
    """
    import random as r

    alphabet = '0123456789abcdef'
    colors = []

    if mode == 'RGB':
        for color in range(count):
            col = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
            colors.append(col)
    else:
        for color in range(count):
            col = '#'
            for i in range(6):
                col += r.choice(alphabet)
            colors.append(col)
    return colors


rgb_colors = make_colors_list(30, 'RGB')
hex_colors = make_colors_list(10)

print(rgb_colors)
print(hex_colors)