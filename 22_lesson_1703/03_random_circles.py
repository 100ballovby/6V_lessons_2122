from turtle import *
import random as r

colors = ['#e05eb3', '#7deb5b', '#5bdaeb', '#eba35b',
          '#eb675b', '#5ba8eb', '#e027f5', '#f52768']

t = Turtle()
t.shape('turtle')

t.hideturtle()  # спрятать черепашку
t.speed(0)

for i in range(1000):
    x = r.randint(-450, 450)  # случайная координата х
    y = r.randint(-450, 450)  # случайная координата у
    rad = r.randint(20, 70)  # случайное значение радиуса

    t.up()
    t.goto(x, y)
    t.down()
    t.color(r.choice(colors))  # choice(seq) достает случайное значение из коллекции seq
    t.dot(rad)  # рисую круг (закрашенный) с радиусом rad

done()