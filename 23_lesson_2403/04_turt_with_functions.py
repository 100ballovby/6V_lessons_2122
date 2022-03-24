from turtle import *
from hw_function import make_colors_list
import random as r

t = Turtle()
colors = make_colors_list(50)

for i in range(30):
    t.up()
    t.goto(r.randint(-400, 400), r.randint(-400, 400))
    t.color(r.choice(colors))
    t.down()
    t.dot(40)

done()

