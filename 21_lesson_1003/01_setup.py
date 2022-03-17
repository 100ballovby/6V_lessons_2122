import pygame as pg
from pygame.draw import rect, circle, polygon

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

W = 700
H = 1000
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

img0 = pg.image.load('Asset 12.png')
rect0 = img0.get_rect()

center = W // 2, 1000
img = img0
rect1 = img.get_rect()
rect1.center = center

angle = 0  # поворот картинки
scale = 0.4  # увеличение картинки
img = pg.transform.rotozoom(img0, angle, scale)

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        angle = -30
        rect1.x += 5
        img = pg.transform.rotozoom(img0, angle, scale)
    elif keys[pg.K_LEFT]:
        angle = 30
        rect1.x -= 5
        img = pg.transform.rotozoom(img0, angle, scale)
    else:
        angle = 0
        img = pg.transform.rotozoom(img0, angle, scale)


    # рисуем тут
    screen.fill(GRAY)
    screen.blit(img, rect1)
    rect(screen, RED, rect1, 1)
    pg.display.update()


    if rect1.collidepoint(W, 950):
        rect1.center = W - 200, 950
    if rect1.collidepoint(0, 950):
        rect1.center = 200, 950