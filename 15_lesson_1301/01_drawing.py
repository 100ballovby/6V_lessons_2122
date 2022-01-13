import pygame as pg
from pygame.draw import rect, circle, polygon

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
end = False

# нарисуем прямоугольник
rect(screen, (191, 25, 78), [10, 10, 100, 75])
rect(screen, (110, 190, 255), [120, 10, 100, 75], 4)
# где_рисуем, (цвет в RGB), [x, y, ширина, высота], толщина_линии

# нарисуем круг
circle(screen, (255, 191, 40), [70, 150], 50)
circle(screen, (255, 191, 40), [70, 150], 70, 5)
# где_рисуем, (цвет в RGB), [x, y], радиус, толщина_линии

# нарисуем треугольник
polygon(screen, (100, 191, 60), [[100, 280], [350, 280], [260, 190]])
polygon(screen, (100, 191, 60), [[100, 280], [350, 280], [260, 370]], 1)
# где_рисуем, (цвет в RGB), [[x1, y1], [x2, y2], [x3, y3]], толщина_линии

x_cor = 350
y_cor = 10
for i in range(10):
    rect(screen, (180, 15, 180), [x_cor, y_cor, 43, 43], 2)
    circle(screen, (255, 255, 255), [x_cor + 21.5, y_cor + 21.5], 15)
    y_cor += 45
    x_cor += 45

pg.display.update()
while not end:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    pg.display.update()


