#coding:utf-8
import pygame
from pygame.locals import *
'''
游戏中的机制：碰撞问题

1、游戏界面中的类
2、敌方飞机（普通飞机、boss飞机）
3、子弹
4、道具（血量、生命、炸弹、无敌）
首先有画面（背景）
然后我方飞机（移动，发射子弹，放道具。。。）
敌方飞机（上下移动）
Boss（左右移动）
发射子弹判断碰撞问题
加分
暂停
'''
SCREEN_WIDTH=480
SCREEN_HEIGHT=800
#子弹类(继承自pygame的精灵类，有常用的图案、速度、区域大小等属性)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):
        super(Bullet,self).__init__()#
        self.image=bullet_img
        #rect矩形，对象看作一个矩形，有一些相关大小的位置参数
        self.rect=self.image.get_rect()
        #下方、中间的位置,init_pos=[100,200],初始化子弹的位置
        self.rect.midbottom=init_pos
        #设置子弹的速度    移动的时候纵坐标增加的位置
        self.speed=10
    #子弹移动方法
    def moveUp(self):# 我方飞机子弹移动方法
        #子弹距离上面的位置越来越小
        self.rect.top-=self.speed
    def moveDown(self):#敌方飞机子弹移动方法
        #子弹距离上面的位置越来越小
        self.rect.top+=self.speed
#我方飞机
class Hero(pygame.sprite.Sprite):
    #shoot是素材的大图，我方飞机有正常状态和被击中状态
    def __init__(self,shoot,hero_rects,init_pos):
        super(Hero,self).__init__()
        self.image = []     #我方飞机的图片定义为一个列表，因为有多种状态
        #hero_rects是一个列表，储存不同状态飞机的宽高属性，要从大图中截取图片和某些数据
        for i in range(len(hero_rects)):
            #shoot.subsurface()从大图中得到某部分图片
            #shoot.subsurface(hero_rects[i])得到图片
            #convert_alpha()  填充，画图
            self.image.append(shoot.subsurface(hero_rects[i]).convert_alpha())
            self.rect=hero_rects[0]
            self.rect.topleft=init_pos
            self.speed=8
            self.bengnum=0
            #发射的子弹要存放到某处
            #pygame.sprite.Group()   用来管理大量的实体类   是一个容器
            self.bullets=pygame.sprite.Group()
            #我方飞机是否被击中
            self.is_hit=False
    def shoot(self,bullet_img):
        #把我方飞机上方，中间的值传给子弹的初始位置
        bullet=Bullet(bullet_img,self.rect.midtop)
        self.bullets.add(bullet)
            
    def moveDown(self):
        if self.rect.top>=SCREEN_HEIGHT-self.rect.height:
            self.rect.top=SCREEN_HEIGHT-self.rect.height
        else:
            self.rect.top+=self.speed
    def moveUp(self):
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top-=self.speed
    def moveLeft(self):
        if self.rect.left<=0:
            self.rect.left=0
        else:
            self.rect.left-=self.speed
    def moveRight(self):
        if self.rect.left>=SCREEN_WIDTH-self.rect.width:
            self.rect.left=SCREEN_WIDTH-self.rect.width
        else:
            self.rect.left+=self.speed
class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_img,enemy_down_img,init_pos):
        super(Enemy,self).__init__()
        #
        self.image=enemy_img
        self.enemy_down_img=enemy_down_img
        self.rect=self.image.get_rect()
        self.rect.topleft=init_pos
        self.speed=2
        self.HP=150
        self.isMove=True
        self.bullets=pygame.sprite.Group()
    def move(self):
        self.rect.top+=self.speed
    def shoot(self,bullet_img):
        bullet=Bullet(bullet_img,self.rect.midbottom)
        self.bullets.add(bullet)
    def moveLeft(self):
        if self.rect.left<=0:
            self.isMove=True
        else:
            self.rect.left-=self.speed
    def moveRight(self):
        if self.rect.left>=SCREEN_WIDTH-self.rect.width:
            self.isMove=False
        else:
            self.rect.left+=self.speed








            
