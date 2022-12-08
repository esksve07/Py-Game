import pygame as pg
from random import randint
from sprites import*

class Game ():
    def __init__(self):  #kjører når vi starter spillet
        pg.init()

        self.WIDTH =1500
        self.HEIGHT = 1200

        self.BLACK = (0,0,0)

        self.screen=pg.display.set_mode((self.WIDTH,self.HEIGHT))



        self.bg = pg.image.load("Background.png")
        self.bg = pg.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))



        self.debug_font = pg.font.SysFont("debug-font", 100)
        self.FPS = 120
        self.clock = pg.time.Clock()

        self.new()

    def new(self):  #ny runde
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectile_grp = pg.sprite.Group()

        self.bg_x = 0
        self.bg_y = 0
        self.hero = Player(self)
        self.enemy = Enemy(self)
        self.attack = Ranged_attack()

        self.all_sprites.add(self.hero, self.enemy)
        self.enemies.add(self.enemy)


        self.text_hp = self.debug_font.render("HP:"+str(self.hero.hp), False, self.BLACK)
        self.run()



    def run(self):  #
        playing = True
        while playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    playing=False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.new()


            self.screen.blit(self.bg,(0, 0))

            self.all_sprites.update()


            hits = pg.sprite.spritecollide(self.hero, self.enemies, True)
            if hits:
                self.hero.hp -=10
                self.text_hp = self.debug_font.render("HP:" + str(self.hero.hp), False, self.BLACK)
                if self.hero.hp <=0:
                    self.hero.kill()
                    self.hero = Player()
                    self.all_sprites.add(self.hero)


            hits = pg.sprite.spritecollide(self.enemies, self.attack, True)
            if hits:
                self.enemy.hp -=10
                if self.enemy.hp <=0:
                    self.enemy.kill()




            if len(self.enemies)<3:
                self.enemy = Enemy()
                self.all_sprites.add(self.enemy)
                self.enemies.add(self.enemy)




            self.all_sprites.draw(self.screen)


            self.screen.blit(self.text_hp, (10,10))
            
            pg.display.update()

g=Game() 