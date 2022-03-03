import pygame as pg
from pygame.draw import rect, circle, polygon

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

img0 = pg.image.load('angry-birds.png').convert_alpha()
rect0 = img0.get_rect()
rect(img0, GREEN, rect0, 1)

center = W // 2, H // 2
img = img0
rect1 = img.get_rect()
rect1.center = center

angle = 0  # поворот картинки
scale = 1  # увеличение картинки

mouse = pg.mouse.get_pos()  # фиксирую позицию мышки

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                if event.mod and pg.KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img = pg.transform.rotozoom(img0, angle, scale)
            if event.key == pg.K_s:
                if event.mod and pg.KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pg.transform.rotozoom(img0, angle, scale)

            if event.key == pg.K_h:
                img = pg.transform.flip(img, True, False)  # что вращать, по_иксу, по_игреку

            rect1 = img.get_rect()
            rect1.center = center

    # рисуем тут
    screen.fill(GRAY)
    screen.blit(img, rect1)
    rect(screen, RED, rect1, 1)
    pg.display.update()