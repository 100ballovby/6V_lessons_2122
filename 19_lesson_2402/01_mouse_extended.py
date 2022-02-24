import pygame as pg
from pygame.draw import rect, circle, polygon

W = 1280
H = 720
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # если нажаои левую кнопку
                circle(screen, RED, event.pos, 20)
                pg.display.update()
            elif event.button == 3:  # если нажали правую кнопку
                circle(screen, BLUE, event.pos, 30)
                rect(screen, GREEN, [event.pos[0]-15, event.pos[1]-15, 30, 30])
                pg.display.update()
            elif event.button == 2:  # если нажали на колесико
                screen.fill(WHITE)
                pg.display.update()

    # рисуем тут
    pg.display.update()