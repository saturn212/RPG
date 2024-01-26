import pygame as pg
import os
import sys
from math import sin, cos, radians


pg.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
lvl = 'game'
font = pg.font.SysFont('aria', 30)
BLaCK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

from load import *
class Topor(pg.sprite.Sprite):
    def __init__(self, image, pos, start_deg):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.deg_rotate = 0
        self.deg = start_deg
        self.timer_atack = 0

    def rotate(self):
        self.deg_rotate -= 20
        self.image = pg.transform.rotate(topor_image, self.deg_rotate)

    def moove(self):
        self.deg += 3
        self.rect.centerx = 150 * cos(radians(self.deg)) + player.rect.centerx
        self.rect.centery = 150 * sin(radians(self.deg)) + player.rect.centery
    def update(self):
        self.rotate()
        self.moove()



class Player(pg.sprite.Sprite):
    def __init__(self, image, pos,):
        pg.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.key = pg.key.get_pressed()
        self.speed = 5
        self.timer_anime = 0
        self.anime = False
        self.frame = 0
        self.pos_maps = [0, 0]
        self.score = 0
        self.topor = 2
        self.camera = False
        self.dir = 'bottom'
        self.add_topor()
    def add_topor(self):
        global topor_group
        topor_group = pg.sprite.Group()
        for i in range(self.topor):
            topor = Topor(topor_image, (self.rect.centerx + 70, self.rect.centery + 70), (360 // self.topor * i))
            topor_group.add(topor)

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image1) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def update(self):
        self.animation()

        key = pg.key.get_pressed()
        if key[pg.K_w]:
            self.image = player_image2[self.frame]
            self.rect.y -= self.speed
            self.dir = "top"
            self.anime = True
            if self.rect.top < 300:
                self.pos_maps[0] += self.speed
                camera_group.update(0, self.speed)
                self.rect.top = 300
                self.camera = True
            else:
                self.camera = False
        elif key[pg.K_a]:
            self.image = player_image3[self.frame]
            self.rect.x -= self.speed
            self.dir = "left"
            self.anime = True
            if self.rect.left < 300 and self.pos_maps[0] < 0:
                self.pos_maps[0] += self.speed
                camera_group.update(self.speed, 0)
                self.rect.left = 300
                self.camera = True
            else:
                self.camera = False
        elif key[pg.K_s]:
            self.image = player_image1[self.frame]
            self.rect.y += self.speed
            self.dir = "bottom"
            self.anime = True
            if self.rect.bottom > 600:
                self.pos_maps[0] += self.speed
                camera_group.update(0, -self.speed)
                self.rect.bottom = 600
                self.camera = True
            else:
                self.camera = False
        elif key[pg.K_d]:
            self.image = player_image4[self.frame]
            self.rect.x += self.speed
            self.dir = "right"
            self.anime = True
            if self.rect.right > 900 and self.pos_maps[0] > -6800:
                self.pos_maps[0] += self.speed
                camera_group.update(-self.speed, 0)
                self.rect.right = 900
                self.camera = True
            else:
                self.camera = False
        else:
            self.camera = False
            self.anime = False
            self.image = player_image1[0]






class Block(pg.sprite.Sprite):

    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy

        if pg.sprite.spritecollide(self, player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            elif player.dir == "top":
                player.rect.top = self.rect.bottom

            elif player.dir == "bottom":
                player.rect.bottom = self.rect.top
            elif player.dir == "right":
                player.rect.right = self.rect.left


class Water(pg.sprite.Sprite):

    def __init__(self, image, pos):

        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
        if pg.sprite.spritecollide(self, player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            elif player.dir == "top":
                player.rect.top = self.rect.bottom
            elif player.dir == "bottom":
                player.rect.bottom = self.rect.top
            elif player.dir == "right":
                player.rect.right = self.rect.left

class Spawner (pg.sprite.Sprite):

    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
        if pg.sprite.spritecollide(self, player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            elif player.dir == "bottom":
                player.rect.bottom = self.rect.top
            elif player.dir == "right":
                player.rect.right = self.rect.left

class Spider (pg.sprite.Sprite):

    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



def lvlGAME():
    screen.fill(BLaCK)
    player_group.update()
    player_group.draw(screen)
    block_group.draw(screen)
    topor_group.update()
    spawner_group.draw(screen)
    spider_group.update()
    spider_group.draw(screen)
    water_group.draw(screen)
    topor_group.draw(screen)
    if not player.camera:

        block_group.update(0, 0)

        water_group.update(0, 0)

        spawner_group.update(0, 0)
    pg.display.update()

def DrawMaps(nameFile):
    maps = []
    source = "gamelvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 100):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    print(maps)
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 40
        for j in range(0, len(maps[0])):
            pos[0] = 40 * j
            if maps[i][j] == '2':
                block = Block(block_image, pos)
                block_group.add(block)
                camera_group.add(block)
            elif maps[i][j] == '1':
                water = Water(water_image, pos)
                water_group.add(water)
                camera_group.add(water)
            elif maps[i][j] == '3':
                spawner = Spawner(spawner_image, pos)
                spawner_group.add(spawner)
                camera_group.add(spawner)
            elif maps[i][j] == '6':
                spider = Spider(spider_image, pos)
                spider_group.add(spider)


def restart():
    global player_group,topor_group, block_group, water_group, spawner_group, spider_group, camera_group,player
    topor_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    block_group = pg.sprite.Group()
    water_group = pg.sprite.Group()
    spawner_group = pg.sprite.Group()
    spider_group = pg.sprite.Group()
    camera_group = pg.sprite.Group()

    player = Player(player_image1[0], (300, 300))
    player_group.add(player)

restart()





DrawMaps('1.txt')
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if lvl == "game":
        lvlGAME()
    elif lvl == "exit":
        pg.quit()
        sys.exit()
    clock.tick(FPS)

