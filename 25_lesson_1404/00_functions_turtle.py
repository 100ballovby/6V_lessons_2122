from turtle import *


def x_angle(obj, col, leng, sides, x, y):
    """
    Функция x_angle рисует ЛЮБОЙ многоугольник
    :param obj: черепашка-объект
    :param col: цвет
    :param leng: длина стороны многоугольника
    :param sides: количество сторон
    :param x: координата по иксу
    :param y: координата по игреку
    :return: None
    """
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.color(col)
    for line in range(sides):
        obj.fd(leng)
        obj.lt(360 / sides)


t = Turtle()
t.shape('turtle')

x_angle(t, 'DarkOliveGreen1', 40, 3, 100, 100)
x_angle(t, 'DarkOliveGreen1', 40, 4, -100, -100)
x_angle(t, 'DarkOliveGreen1', 40, 7, 10, 50)
x_angle(t, 'DarkOliveGreen1', 40, 6, -120, 90)
x_angle(t, 'DarkOliveGreen1', 40, 13, -90, -90)

done()
