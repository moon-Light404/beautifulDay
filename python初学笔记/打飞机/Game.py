#coding:utf-8
from pygame.locals import *
from GameObj import *
import os,sys
import time
import random
wudi=False
shoot_times=0#
score=0#
flagx=1#
shoot_times2=0#big放子弹计时器
beng_time=0#炸弹移动频率
#初始化游戏
pygame.init()
#创建一个屏幕   set_mode((width,height))
screen=pygame.display.set_mode((480,700))
#设置标题
pygame.display.set_caption('打飞机游戏')
#载入背景图片  pygame.image.load直接读取图片
background_img=pygame.image.load('data\\img\\background.png')
#得到相关的矩形参数
background_img_rect=background_img.get_rect()
#载入游戏结束的背景图片
game_over_img=pygame.image.load('data\\img\\gameover.png')
#得到相关的矩形参数
game_over_img_rect=game_over_img.get_rect()
#载入shoot大图
shoot=pygame.image.load('data\\img\\shoot.png')
#载入音效    pygame.mixer.music.load直接运行
game_music_sound=pygame.mixer.music.load('data\\audio\\game_music.wav')
#初始化音乐相关参数    play(loops=0 -1表示一直重复,start=0,秒数)
pygame.mixer.music.play(-1,0.0)
#设置音量   0-1  1最大
pygame.mixer.music.set_volume(0.5)
#玩家飞机在shoot中的位置列表
hero_rects=[]
hero_recten=[]
#pygame.Rect(left,top,width,height)
hero_rects.append(pygame.Rect(0,100,105,130))#
hero_rects.append(pygame.Rect(175,245,105,130))  #被击中时的敌机
hero_pos=[0,500]  #玩家飞机的初识位置

#构造一个
big_rects=[]
hero=Hero(shoot,hero_rects,hero_pos)
big_rects.append(pygame.Rect(149,1024-270,174,239))

big_rects.append(pygame.Rect(149+520,497,174,239))
big_pos=[180,0]
big=Big(shoot,big_rects,big_pos)
#得到子弹的图片
bullet_rect=pygame.Rect(1004,987,13,24)
bullet_img=shoot.subsurface(bullet_rect) #得到子弹图片，还未画出来
#炸弹
# beng_rect=pygame.Rect(105,118,62,111)
# beng_img=shoot.subsurface(beng_rect)
# beng=Beng(beng_img,(240,0))
#敌方飞机
enemy1_rect=pygame.Rect(535,620,50,36)
enemy1_img=shoot.subsurface(enemy1_rect)

enemy1_down_rect=pygame.Rect(270,360,50,36)
enemy1_down_img=shoot.subsurface(enemy1_down_rect)
#敌机的精灵组
enemies1_down=pygame.sprite.Group()
enemies1=pygame.sprite.Group()
boss=pygame.sprite.Group()
boss.add(big)
# benged=pygame.sprite.Group()
# benged.add(beng)
enemies_times=0
# 载入游戏结束的背景图片
game_over_img = pygame.image.load('data\\img\\gameover.png')
# 得到相关的矩形参数
game_over_img_rect = game_over_img.get_rect()

#游戏开始的方法
running=True
while running:
    #判断用户是否点击了关闭按钮:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()  #系统的退出方法
    '''
            帧速率，是指程序每秒在屏幕中绘制图像的数目，用FPS来表示
            一般都能达到每秒60帧，越低越卡
    '''
    pygame.time.Clock().tick(60)
    
    #绘制背景
    screen.fill(55) #设置屏幕的颜色  fill(RGB)
    #blit(背景图，位置)
    screen.blit(background_img,background_img_rect)
    key_pressed=pygame.key.get_pressed()
    if key_pressed[K_SPACE]:
        if not hero.is_hit:
            if shoot_times==5:
                hero.shoot(bullet_img) 
            shoot_times+=1
            if shoot_times>5:
                shoot_times=0
    
    for bullet in hero.bullets:
        bullet.moveUp()
        if bullet.rect.top<0:
            hero.bullets.remove(bullet)
    hero.bullets.draw(screen)
    #boss
   
    #敌机
    if enemies_times%50==0:
        enemy1_pos=[random.randint(0,SCREEN_WIDTH-enemy1_rect.width),0]
        enemy1=Enemy(enemy1_img,enemy1_down_img,enemy1_pos)
        enemies1.add(enemy1)
    enemies_times+=1
    if enemies_times>50:
        enemies_times=0
    #移动敌机
    for enemy1 in enemies1:
        enemy1.move()
        if pygame.sprite.collide_circle(enemy1,hero):
            enemies1_down.add(enemy1)
            enemies1.remove(enemy1)
            hero.is_hit=True
            break
        if enemy1.rect.top>SCREEN_HEIGHT:
            enemies1.remove(enemy1)
    collisions=pygame.sprite.groupcollide(enemies1,hero.bullets,True,True)
    for enemy1_down in collisions:
        enemies1_down.add(enemy1_down)
    for i in enemies1_down:#得分
        enemies1_down.remove(i)
        score+=10

    #画boss

    if score>200:
        if big.is_hit>0:
            if  big.is_hit:
                screen.blit(big.image[0],big.rect)
            else:
                screen.blit(big.image[1],big.rect)
            if big.flagrl:
                big.moveRight()
            else:
                big.moveLeft()
            # big.move()
#           #big 画子弹
            if shoot_times2==60:
                big.shoot(bullet_img) 
            shoot_times2+=1
            if shoot_times2>60:
                shoot_times2=0
    
            for bullet in big.bullets:
                bullet.moveDown()
            big.bullets.draw(screen)
#            
            collisions=pygame.sprite.groupcollide(boss,hero.bullets,False,True)#让子弹消失
            #big和hero碰撞gameover
            if pygame.sprite.collide_circle(big,hero):
                break
            for i in hero.bullets:
                if pygame.sprite.collide_circle(big,i):
                    hero.bullets.remove(i)
                    big.is_hit-=1
        if big.is_hit<=0 and flagx==1:#得分100
            screen.blit(big.image[1],big.rect)
            pygame.display.update()
            #time.sleep(9)
            flagx=0
            score+=100

    for i in big.bullets:#big的子弹和hero碰撞gameover
        if pygame.sprite.collide_circle(hero,i):
            hero.is_hit=True

    key_pressed=pygame.key.get_pressed()
    if key_pressed[K_p]and hero.wudi==1:
        big.is_hit-=15#减big血
        enemies1.empty()
    #绘制我方飞机
    if not hero.is_hit:
        screen.blit(hero.image[0],hero.rect)
    else:
        screen.blit(hero.image[1],hero.rect)
        running=False
    #绘制敌机
    enemies1.draw(screen)
    #画分
    score_font=pygame.font.Font('data\\font\\CHILLER.TTF',36)
    score_text=score_font.render(str(score),True,(240,0,87))
    score_text_rect=score_text.get_rect()
    screen.blit(score_text,score_text_rect)
    #更新屏幕
    pygame.display.update()
    key_pressed=pygame.key.get_pressed()
    if not hero.is_hit:
        if key_pressed[K_UP] or key_pressed[K_w]:
            hero.moveUp()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            hero.moveDown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            hero.moveLeft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            hero.moveRight()
screen.blit(game_over_img, game_over_img_rect)
# 更新屏幕，屏幕内容有更改就要更新屏幕
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()    