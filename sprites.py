import pygame as pg
from random import randint 
vec = pg.math.Vector2


player_img = pg.image.load("Finn right.png")
player_img = pg.transform.scale(player_img, (100, 125))
player_img_left = pg.image.load("Finn Left.png")
player_img_left = pg.transform.scale(player_img_left, (100, 125))

player_img_up = pg.image.load("Finn up.png")
player_img_up = pg.transform.scale(player_img_up, (100, 125))
player_img_down = pg.image.load("Finn down.png")
player_img_down = pg.transform.scale(player_img_down, (100, 125))



enemy_img = pg.image.load("Minotaur right.png")
enemy_img = pg.transform.scale(enemy_img, (260, 205))
enemy_img_left = pg.image.load("Minotaur left.png")
enemy_img_left = pg.transform.scale(enemy_img_left, (260, 205))

banana_attack = pg.image.load("banana.png")
banana_attack = pg.transform.scale(banana_attack, (64,64))



class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups =  game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,800)
        self.rect.center = self.pos
        self.speed = 3
        self.hp = 100
        self.moving_right = True
        self.kills = 0


       


    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -=self.speed
            self.image = player_img_up
            self.game.bg_y += 1

        if keys[pg.K_s]:
            self.pos.y +=self.speed
            self.image = player_img_down
            self.game.bg_x -= 1

        if keys[pg.K_a]:
            self.pos.x -=self.speed
            self.image = player_img_left
            self.game.bg_y -= 1
            self.moving_right = False

        if keys[pg.K_d]:
            self.pos.x +=self.speed
            self.image = player_img
            self.game.bg_x += 1
            self.moving_right = True


        if keys[pg.K_SPACE]:
            self.attack()
            



        if self.pos.x > 1450:
            self.pos.x = 1450
        if self.pos.y > 1140:
            self.pos.y = 1140
        if self.pos.x < -50:
            self.pos.x = -50
        if self.pos.y < -50:
            self.pos.y = -50







    def attack(self):
        if self.moving_right == True:
            self.attack_spawn_x = self.rect.right
        else:
            self.attack_spawn_x = self.rect.left
        self.attack_object = Ranged_attack(self.game, self.attack_spawn_x, self.pos.y)



class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img_left
        self.rect = self.image.get_rect()
        self.pos = vec(300,300)
        self.rect.center = self.pos
        self.speed = 7

    def update(self):

        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -100:
            self.pos.x = 1400
            self.pos.y = randint(0,450)



class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game,x,y):
        self.groups = game.all_sprites, game.projectile_grp
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = banana_attack
        self.rect = self.image.get_rect()
        self.pos = vec(x,y+25)
        self.speed = 5

        self.rect.center = self.pos
        self.move_to = vec(pg.mouse.get_pos()) # finner posisjon til musepeker
        self.move_vector = self.move_to - self.pos  # finner "forskjellen" mellom self.pos og posisjon til musepeker



    def update(self):
        self.pos += self.move_vector.normalize() * self.speed  #
        
        self.rect.center = self.pos
       
       
        if self.pos.x > 1600:
            self.kill
        if self.pos.y > 1300:
            self.kill
        if self.pos.x > -100:
            self.kill
        if self.pos.y > -100:
            self.kill