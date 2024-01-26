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
        elif key[pg.K_a]:
            self.image = player_image3[self.frame]
            self.rect.x -= self.speed
            self.dir = "left"
            self.anime = True
        elif key[pg.K_s]:
            self.image = player_image1[self.frame]
            self.rect.y += self.speed
            self.dir = "bottom"
            self.anime = True
        elif key[pg.K_d]:
            self.image = player_image4[self.frame]
            self.rect.x += self.speed
            self.dir = "right"
            self.anime = True
        else:
            self.anime = False












def lvlGAME():
    screen.fill(BLaCK)



    player_group.update()
    player_group.draw(screen)
    topor_group.update()
    topor_group.draw(screen)
    # def startMenu():
    #     screen.fill((122, 122, 122))
    #
    #     button_group.draw(screen)
    #     button_group.update()
    #
    #     pg.display.update()

    # def DrawMaps(nameFile):
    #     maps = []
    #     source = "game lvl/" + str(nameFile)
    #     with open(source, "r") as file:
    #         for i in range(0, 20):
    #             maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    #     print(maps)
    #     pos = [0, 0]
    #     for i in range(0, len(maps)):
    #         pos[1] = i * 40
    #         for j in range(0, len(maps[0])):
    #             pos[0] = 40 * j
    #             if maps[i][j] == '3':
    #                 brick = Brick(brick_image, pos)
    #                 brick_group.add(brick)
    #             elif maps[i][j] == '4':
    #                 bush = Bush(bush_image, pos)
    #                 bush_group.add(bush)
    #             elif maps[i][j] == '2':
    #                 iron = Iron(iron_image, pos)
    #                 iron_group.add(iron)
    #             elif maps[i][j] == '1':
    #                 water = Water(water_image, pos)
    #                 water_group.add(water)
    #             elif maps[i][j] == '6':
    #                 enemy = Enemy(enemy_image, pos)
    #                 enemy_group.add(enemy)
    #             elif maps[i][j] == '5':
    #                 flag = Flag(flag_image, pos)
    #                 flag_group.add(flag)
    #
    pg.display.update()

def restart():
    global player_group,topor_group, player
    topor_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    player = Player(player_image1[0], (300, 300))
    player_group.add(player)







restart()
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

