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
        elif event.type == pg.KEYDOWN:  # если нажали кнопку
            print(f'Button {pg.key.name(event.key)} pressed!')  # написать название кнопки
            if event.key == pg.K_RIGHT:  # если нажали кнопку стрелка_вправо
                motion = RIGHT
            elif event.key == pg.K_LEFT:  # если нажали кнопку стрелка_влево
                motion = LEFT
        elif event.type == pg.KEYUP:  # если кнопку отпустили
            print(f'Button {pg.key.name(event.key)} released!')
            if event.key in [pg.K_LEFT, pg.K_RIGHT]:
                motion = STOP

    s.fill(BLUE)
    circle(s, ORANGE, [circle_x, circle_y], r)
    pg.display.update()

    if motion is LEFT:
        circle_x -= 5
    elif motion is RIGHT:
        circle_x += 5

