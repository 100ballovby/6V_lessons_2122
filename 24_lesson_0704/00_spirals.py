from turtle import *
import random as r


def make_colors_list(count):
    """
    Функция создает список кодов цветов,
    в палитреHEX.
    :param count: количество цветов в списке
    :return: list: список цветов
    """
    import random as r
    alphabet = '0123456789abcdef'
    colors = []
    for color in range(count):
        col = '#'
        for i in range(6):
            col += r.choice(alphabet)
        colors.append(col)
    return colors


colors = make_colors_list(10000)
colors.sort()
t = Turtle()
t.speed(0)


def spiral(obj, angle):
    length = 5
    for i in range(200):
        obj.fd(length)
        obj.rt(angle)
        length += 2
        obj.color(r.choice(colors))

spiral(t, 172)

done()
