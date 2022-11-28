import pygame as pg
import random
from sprites import *

pg.init()



BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
GREEN=(132, 181, 159)

WIDTH =1500
HEIGHT = 1200

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

hero = Player()
enemy = Enemy()
all_sprites.add(hero, enemy)
enemies.add(enemy)

screen=pg.display.set_mode((WIDTH,HEIGHT))

bg = pg.image.load("Background.png")
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))



FPS = 144
clock = pg.time.Clock()

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            playing=False



    screen.blit(bg,(0, 0))

    all_sprites.update()


    hits = pg.sprite.spritecollide(hero, enemies, True)
    if hits:
        hero.hp -=10
        if hero.hp < 0:
            pass

    if len(enemies)<2:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)




    all_sprites.draw(screen)
    
    pg.display.update()