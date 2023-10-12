import pygame as pg
pg.init()
FPS = 60
Time = pg.time.Clock()
screen = pg.display.set_mode((600, 800))
pg.display.set_caption("Hello")
# pg.display.set_icon("")
running = True
while running:
    screen.fill('blue') # set background
    Time.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT: running = False
    pg.display.flip()
pg.quit()
