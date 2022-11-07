import pygame as pg
import random

pg.init()

screen=pg.display.set_mode((800,600))
player_img = pg.image.load("player.png")
player_img = pg.transform.scale(player_img, (100, 125))

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
GREEN=(132, 181, 159)

x = 0
y = 0

speed = 10

direction_x=1
direction_y=1

FPS = 144
clock = pg.time.Clock()

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            playing=False



    screen.fill(BLUE)

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed
        print("Up")

    if keys[pg.K_s]:
        y += speed
        print("Down")

    if keys[pg.K_a]:
        x -= speed
        print("Left")

    if keys[pg.K_d]:
        x += speed
        print("Right")

    if x > 700:
        x = 700
    if y > 475:
        y = 475
    if x < 0:
        x = 0
    if y < 0:
        y = 0



    screen.blit(player_img, (x,y))
    
    pg.display.update()