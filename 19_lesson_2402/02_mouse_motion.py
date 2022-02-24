import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

pg.mouse.set_visible(False)  # спрятать курсор мыши

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    screen.fill((255, 255, 255))
    if pg.mouse.get_focused():  # если курсор мыши находится над экраном игры
        pos = pg.mouse.get_pos()  # фиксирую координаты мыши в переменной
        rect(screen, (0, 255, 0), [pos[0] - 10, pos[1] - 10, 20, 20])  # рисую квадрат в том же месте, где находится мышка

    # рисуем тут
    pg.display.update()