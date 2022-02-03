import pygame as pg
from pygame.draw import rect, circle, polygon

W = 700
H = 300
WHITE = (255, 255, 255)
BLUE = (0, 70, 255)
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'
STOP = 'stop'

x = W // 2
y = H // 2
r = 50

motion = STOP

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                motion = RIGHT
            elif event.key == pg.K_LEFT:
                motion = LEFT
            elif event.key == pg.K_UP:
                motion = UP
            elif event.key == pg.K_DOWN:
                motion = DOWN
        elif event.type == pg.KEYUP:
            if event.key in [pg.K_LEFT, pg.K_RIGHT, pg.K_DOWN, pg.K_UP]:
                motion = STOP

    screen.fill(WHITE)
    circle(screen, BLUE, [x, y], r)
    # рисуем тут
    pg.display.update()

    if motion == RIGHT:
        x += 3
    elif motion == LEFT:
        x -= 3
    elif motion == UP:
        y -= 3
    elif motion == DOWN:
        y += 3
    elif motion == STOP and x != W // 2:
        if x < W // 2:
            x += 5
        else:
            x -= 5
    elif motion == STOP and y != H // 2:
        if y < H // 2:
            y += 5
        else:
            y -= 5
