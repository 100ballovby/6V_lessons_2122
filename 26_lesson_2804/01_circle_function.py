from turtle import *


def draw_circle(obj, x, y, radius, deg=360):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.circle(radius, deg)

t = Turtle()
draw_circle(t, 100, -200, 50, 180)

done()
