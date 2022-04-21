from turtle import *


def lines(obj, lin):
    length = 100
    for i in range(lin):
        obj.lt(90)
        obj.fd(length)
        obj.bk(length)
        obj.rt(90)
        obj.up()
        obj.fd(10)
        obj.down()


def cross(obj, len):
    for i in range(4):
        obj.fd(len)
        obj.lt(90)
        obj.fd(len)
        obj.rt(90)
        obj.fd(len)
        obj.rt(90)


t = Turtle()
