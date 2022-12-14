import pygame as pg
from random import randint
from sprites import*

class Game ():
    def __init__(self):  #kjører når vi starter spillet
        pg.init()



        pg.mixer.music.load('Music.flac')
        pg.mixer.music.play(-15)

        self.WIDTH =1500
        self.HEIGHT = 1200

        self.BLACK = (0,0,0)
        self.RED = (255,0,0)


        self.screen=pg.display.set_mode((self.WIDTH,self.HEIGHT))



        self.bg = pg.image.load("Background.png")
        self.bg = pg.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))


        self.yourmurderer_bb_font = pg.font.SysFont("yourmurderer-bb-font", 100)
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
        self.enemy = Enemy()


        self.all_sprites.add(self.hero, self.enemy)
        self.enemies.add(self.enemy)



        self.run()


    def gameover_loop(self):

        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.yourmurderer_bb_font.render("Game over, click R to restart", False, (self.RED))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()


                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:  # om vi clicker på R, avslutter vi game over loop, og går derett til self.new() som ligger etter game_over loop
                        self.game_over = False  

        self.screen.fill(self.BLACK)
        self.blit(self.game_over_text,(30,30))  # tegner tekst på skjerm. 
 
        pg.display.update()


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



            self.projectile_grp_hits = pg.sprite.groupcollide(self.enemies, self.projectile_grp, True, True)





            if self.projectile_grp_hits:
                self.hero.kills += 1



            if len(self.enemies)<3:
                self.enemy = Enemy()
                self.all_sprites.add(self.enemy)
                self.enemies.add(self.enemy)




            self.all_sprites.draw(self.screen)


            self.text_hp = self.debug_font.render("HP:"+str(self.hero.hp), False, self.BLACK)
            self.text_kills = self.debug_font.render("Kills:"+str(self.hero.kills), False, self.BLACK)



            self.screen.blit(self.text_hp, (10,10))
            self.screen.blit(self.text_kills, (10,90))


            pg.display.update()

g=Game() 