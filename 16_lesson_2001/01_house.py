import pygame as pg
from pygame.draw import circle, rect, polygon, ellipse

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
end = False

rect(screen, (100, 100, 190), [0, 0, 640, 288])
ellipse(screen, (0, 180, 0),  [-180, 200, 900, 380])

pg.display.update()
while not end:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    pg.display.update()


