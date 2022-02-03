import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randrange

pg.font.init()  # инициализация (включение) возможности писать
score_font = pg.font.SysFont('akrobat', 20)  # стиль шрифта
score = 0

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

BLUE = (64, 77, 194)
RED = (194, 64, 101)
WHITE = (255, 255, 255)

x1 = 200
y1 = 200
block = 30

enemy_x = round(randrange(0, W - block) / 10) * 10
enemy_y = round(randrange(0, H - block) / 10) * 10

x_change = 0
y_change = 0

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(10)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x_change = block
                y_change = 0
            elif event.key == pg.K_LEFT:
                x_change = -block
                y_change = 0
            elif event.key == pg.K_UP:
                x_change = 0
                y_change = -block
            elif event.key == pg.K_DOWN:
                x_change = 0
                y_change = block

    x1 += x_change
    y1 += y_change

    if (x1 >= W or x1 < 0) or (y1 >= H or y1 < 0):
        finished = True

    screen.fill(WHITE)
    player = rect(screen, BLUE, [x1, y1, block, block])
    enemy = rect(screen, RED, [enemy_x, enemy_y, block, block])

    if player.colliderect(enemy):  # позволяет отследить коллизию квадрата относительно врага
        print('hit')
        # враг будет уходить в другое место
        enemy_x = round(randrange(0, W - block) / 10) * 10
        enemy_y = round(randrange(11, H - block) / 10) * 10  # еда не будет появляться на тексте с очками

        score += 1

    value = score_font.render(f'Your score: {score}', True, (0, 0, 0))  # подготовил текст для отображения
    screen.blit(value, [10, 10])  # Отображаю текст в левом верхнем углу экрана

    # рисуем тут
    pg.display.update()
