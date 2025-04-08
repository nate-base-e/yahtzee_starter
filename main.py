import pygame as pg

pg.init()
screen = pg.display.set_mode((984, 720))
clock = pg.time.Clock()
running = True
dt = 0
totTime = 0
framerate = 60  # fps



while running:
    #screen.blit(background_image, (0, 0))
    pg.display.flip()
