import pygame as pg
from pygame.draw import circle

W = 1280
H = 720

# настроим круг
circle_x = W // 2
circle_y = H // 2
r = 50

# настраиваем движение
RIGHT = 'to the right'
LEFT = 'to the left'
STOP = 'stop'
motion = STOP

# запишем цвета
BLUE = (52, 152, 235)
PINK = (209, 167, 203)
ORANGE = (255, 196, 33)

s = pg.display.set_mode((W, H))
clock = pg.time.Clock()

finished = False
while not finished:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    s.fill(BLUE)
    circle(s, ORANGE, [circle_x, circle_y], r)
    pg.display.update()

    keys = pg.key.get_pressed()  # считывает нажатия всех кнопок на клавиатуре и возвращает True, если какую-то кнопку нажали
    if keys[pg.K_LEFT]:
        circle_x -= 5
    elif keys[pg.K_RIGHT]:
        circle_x += 5
    elif keys[pg.K_UP]:
        circle_y -= 5
    elif keys[pg.K_DOWN]:
        circle_y += 5
    elif keys[pg.K_EQUALS]:
        r += 5
    elif keys[pg.K_MINUS]:
        r -= 5

