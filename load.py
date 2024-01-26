import pygame as pg
from script import load_image
topor_image = pg.image.load('image/topor/1.png').convert_alpha()
player_image1 = load_image('image/player/bottom')
player_image2 = load_image('image/player/top')
player_image3 = load_image('image/player/left')
player_image4 = load_image('image/player/right')
block_image = pg.image.load('image/block/block.jpg').convert_alpha()
water_image = pg.image.load('image/block/water.jpg').convert_alpha()
spawner_image = pg.image.load('image/block/spawner.png').convert_alpha()
spider_image = load_image('image/spider')
