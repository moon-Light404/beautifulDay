# coding:utf-8
import pygame
from pygame.locals import *
import os, sys
import random

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 480


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        super(Bullet, self).__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def moveUp(self):
        self.rect.top -= self.speed

    def moveDown(self):
        self.rect.top += self.speed



class Hero(pygame.sprite.Sprite):
    def __init__(self, shoot, hero_rects, init_pos):
        super(Hero, self).__init__()
        self.image = []
        self.wudi = 0  # 判断无敌
        for i in range(len(hero_rects)):
            self.image.append(shoot.subsurface(hero_rects[i]).convert_alpha())
            self.rect = hero_rects[0]
            self.rect.topleft = init_pos
            self.speed = 8
            self.bengNum = 0
            self.bullets = pygame.sprite.Group()
            self.is_hit = False

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_img, init_pos):
        super(Enemy, self).__init__()
        self.image = enemy_img
        self.enemy_down_img = enemy_down_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.flag = 0
        self.speed = 2
        self.hp = 120#boss的血量
        self.isMoveRight = True
        #boss子弹精灵组
        self.bullets = pygame.sprite.Group()
    #敌机移动
    def move(self):
        self.flag += 1
        if self.flag > 20:
            self.flag = 0
        self.rect.top += self.speed
        a = random.randint(0, 1)
        if self.flag == 20:
            for i in range(10):
                if a:
                    if self.rect.left <= 0:
                        self.rect.left = 0
                    else:
                        self.rect.left -= self.speed
            for i in range(10):
                if a == 0:
                    if self.rect.left >= SCREEN_WIDTH - self.rect.width:
                        self.left = SCREEN_WIDTH - self.rect.width
                    else:
                        self.rect.left += self.speed

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midbottom)
        self.bullets.add(bullet)

    # def move1(self):  # boss移动

    def moveL(self):
        if self.rect.left <=0:
            self.isMoveRight = True
        else:
            self.rect.left -= self.speed
    def moveR(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.isMoveRight = False
        else:
            self.rect.left += self.speed












# class Boss(pygame.sprite.Sprite):
#     def __init__(self, shoot, big_rects, init_pos):
#         super(Boss, self).__init__()
#         self.image = []
#         for i in range(len(big_rects)):
#             self.image.append(shoot.subsurface(big_rects[i]).convert_alpha())
#             self.rect = big_rects[0]
#             self.rect.topleft = init_pos
#             self.speed = 5
#             self.bullets = pygame.sprite.Group()
#             self.is_hit = 30
#             self.flagrl = 0
#
#     def shoot(self, bullet_img):
#         bullet = Bullet(bullet_img, self.rect.midbottom)
#         self.bullets.add(bullet)
#
#     def moveLeft(self):
#         if self.rect.left <= 0:
#             self.rect.left = 0
#             self.flagrl = 1
#         else:
#             self.rect.left -= self.speed
#
#     def moveRight(self):
#         if self.rect.left >= SREEN_WIDTH - self.rect.width:
#             self.rect.left = SREEN_WIDTH - self.rect.width
#             self.flagrl = 0
#         else:
#             self.rect.left += self.speed