import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

pg.mouse.set_visible(False)  # спрятать курсор мыши
img = pg.image.load('cpu.png').convert_alpha()  # загружаю картинку из файла
img_rect = img.get_rect()  # превращаю картинку в объект pygame
img_rect.center = W // 2, H // 2  # выставляю центр изображения посередине экрана
motion = False

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if img_rect.collidepoint(event.pos):  # картинка будет реагировать на положение мышки
                motion = True
        elif event.type == pg.MOUSEBUTTONUP:
            motion = False
        elif event.type == pg.MOUSEMOTION and motion:  # если мышь двигается и motion = True
            img_rect.move_ip(event.rel)  # картинка будет сдвигаться за мышью


    screen.fill((255, 255, 255))
    screen.blit(img, img_rect)  # отображаю картинку в координатах img_rect
    # рисуем тут
    pg.display.update()