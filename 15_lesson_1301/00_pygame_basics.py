import pygame as pg

# настроим окошко игры
screen = pg.display.set_mode((640, 480))  # размер окна 640х480 пикселей
clock = pg.time.Clock()  # отвечает за сменяемость кадров
end = False  # отвечает за работу игры (когда end=True, игра окончена)

# если нужно что-то отобразить на экране игры до запуска
pg.display.update()  # обновить кадры
while not end:  # пока игра не окончена
    clock.tick(30)  # устанавливаю количество кадров в секунду
    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # если нажали на крестик в окне
            end = True  # закончить игру

    pg.display.update()  # обновляю кадры в цикле


