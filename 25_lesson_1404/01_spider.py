from turtle import *


def triangle(obj, leng):
    for i in range(3):
        obj.fd(leng)
        obj.lt(120)


def x_angle(obj, col, leng, legs, x, y):
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
    for line in range(legs):
        obj.fd(leng)
        triangle(obj, 50)
        obj.bk(leng)
        obj.lt(360 / legs)


t = Turtle()
t.shape('turtle')
t.speed(0)
x_angle(t, 'DarkOliveGreen1', 100, 12, 100, 100)


done()
