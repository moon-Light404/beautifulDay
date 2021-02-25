#coding:utf-8
from pygame.locals import *
from youxilei import *#自己的类
import os,sys
import random

#
pygame.init()
#
screen=pygame.display.set_mode((480,800))
pygame.display.set_caption('打飞机游戏')
#载入背景图片，pygame.image.load直接读取图片
background_img=pygame.image.load('data\\img\\background.png')
#
background_img_rect=background_img.get_rect()
#载入游戏结束图片
game_over_img=pygame.image.load('data\\img\\gameover.png')
#
game_over_img_rect=game_over_img.get_rect()
#载入shoot大图
shoot=pygame.image.load('data\\img\\shoot.png')
#载入音量   pygame.mixer.music.load()直接运行
game_music_sound=pygame.mixer.music.load('data\\audio\\game_music.wav')
#初始化音乐相关参数    play(loops=0   -1表示一直重复)
pygame.mixer.music.play(-1,0.0)
#设置音量   0-1   1最大
pygame.mixer.music.set_volume(0.3)
#玩家飞机在shoot中的位置列表
hero_rects=[]
#Pygame.Rect(left,top,width,height)
hero_rects.append(pygame.Rect(0,100,105,120))#正常飞机
hero_rects.append(pygame.Rect(160,245,105,120))#被击中的飞机
hero_pos=[0,500]#玩家飞机初始位置
#构造一个Hero
hero=Hero(shoot,hero_rects,hero_pos)
#得到子弹图片
bullet_rect=pygame.Rect(1004,987,15,24)
bullet_img=shoot.subsurface(bullet_rect)#得到子弹图片，还没画出
#敌方飞机
#敌机图片
enemy1_rect=pygame.Rect(535,610,55,40)
enemy1_img=shoot.subsurface(enemy1_rect)
#
enemy1_down_rect=pygame.Rect(270,360,55,40)
enemy1_down_img=shoot.subsurface(enemy1_down_rect)
#
enemies1=pygame.sprite.Group()
#
enemies1_down=pygame.sprite.Group()

Boss_rect=pygame.Rect(170,750,170,255)
Boss_img=shoot.subsurface(Boss_rect)
pygame.transform.smoothscale(Boss_img,(150,150))
#
Boss_down_rect=pygame.Rect(170,475,170,255)
Boss_down_img=shoot.subsurface(Boss_down_rect)
pygame.transform.smoothscale(Boss_down_img,(150,150))

Boss_group=pygame.sprite.Group()
#
Boss_down_group=pygame.sprite.Group()

#



isBossExist=False
enemies_times=0
#
shoot_times=0
isbeng=0
#
score=0
def dalall():
    for enemy1 in enemies1:
        enemies1_down.add(enemy1)
        enemies1.remove(enemy1)
    for boss in Boss_group: 
        boss.HP=-1     
#游戏开始方法
running=True
while running:
    shoot_times+=1
    #
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()#系统退出方法
    #帧数
    pygame.time.Clock().tick(60)
    
    #发射子弹
    if not hero.is_hit:
        shoot_times+=1
        if shoot_times>=50:
            shoot_times=0
    #子弹移动
    for bullet in hero.bullets:
        bullet.moveUp()
        if bullet.rect.top<0:
            hero.bullets.remove(bullet)
    #生成敌机 
    if enemies_times % 50==0:
        #
        #
        enemy1_pos=[random.randint(0,SCREEN_WIDTH-enemy1_rect.width),0]
        #
        enemy1=Enemy(enemy1_img,enemy1_down_img,enemy1_pos)
        #
        enemies1.add(enemy1)
    enemies_times+=1
    if enemies_times>50:
        enemies_times=0
    #
    for enemy1 in enemies1:
        enemy1.move()
        #
        #
        if pygame.sprite.collide_circle(enemy1,hero):
            #
            enemies1_down.add(enemy1)
            #
            enemies1.remove(enemy1)
            hero.is_hit=True
            break
        if enemy1.rect.top<0:
            enemies1.remove(enemy1)
    #
    collisions=pygame.sprite.groupcollide(enemies1,hero.bullets,True,True)
    #
    for enemy1_down in collisions:
        enemies1_down.add(enemy1_down)

    #Boss生成
    if isbeng%150==0 and isbeng>0 and isBossExist==False:
        isBossExist=True
        Boss_pos=[random.randint(0,SCREEN_WIDTH-Boss_rect.width),0]
        boss=Enemy(Boss_img,Boss_down_img,Boss_pos)
        Boss_group.add(boss) 
    if isbeng%250==0 and isbeng>0 and isBengExist==False:
        isBengExist=True
        Beng_pos=[random.randint(0,SCREEN_WIDTH-Beng_rect.width),0]
        beng=Enemy(Beng_img,Beng_down_img,Beng_pos)
        Beng_group.add(beng) 
            
        
        
    for i in enemies1_down:
        enemies1_down.remove(i)
        score+=10
        isbeng+=10
    for i in Boss_down_group:
        Boss_down_group.remove(i)
        score+=30
        isbeng+=10
    #绘制背景
    screen.fill(0)#
    #
    screen.blit(background_img,background_img_rect)
    
    for boss in Boss_group:
        if boss.isMove:
            boss.moveRight()
        else:
            boss.moveLeft()    
        boss.bullets.draw(screen)
        if enemies_times%50==0:
            boss.shoot(bullet_img)    
        
        for bullet in boss.bullets:
            bullet.moveDown()
            if bullet.rect.top>SCREEN_HEIGHT:
                boss.bullets.remove(bullet)
            if pygame.sprite.collide_circle(bullet,hero):
                boss.bullets.remove(bullet)
                hero.is_hit=True
                break
        for bullet in hero.bullets:
            if pygame.sprite.collide_circle(bullet,boss):
                hero.bullets.remove(bullet)
                boss.HP-=10
                if boss.HP<=0:
                    Boss_down_group.add(boss)
                    Boss_group.remove(boss)
                    isBossExist=False
            if pygame.sprite.collide_circle(boss,hero):
                hero.is_hit=True
                break
    #
        pygame.sprite.groupcollide(boss.bullets,hero.bullets,True,True)

           

        
        
        
    
    
    if not hero.is_hit:
        screen.blit(hero.image[0],hero.rect)
    else:
        screen.blit(hero.image[1],hero.rect)
        break
    #
    hero.bullets.draw(screen)
    #
    enemies1.draw(screen)
    Boss_group.draw(screen)

    score_font=pygame.font.Font('data\\font\\CHILLER.TTF',36)
    #
    score_text=score_font.render(str(score),True,(240,0,87))
    score_text_rect=score_text.get_rect()
    #
    screen.blit(score_text,score_text_rect)
    
    #更新屏幕
    pygame.display.update()

    #
    #
    key_pressed=pygame.key.get_pressed()
    if not hero.is_hit:
        #key_pressed[K_UP]按了方向键上或w
        if key_pressed[K_UP] or key_pressed[K_w]:
            hero.moveUp()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            hero.moveDown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            hero.moveLeft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            hero.moveRight()
        if key_pressed[K_SPACE]  and shoot_times%5==0:
            hero.shoot(bullet_img)

screen.blit(game_over_img,game_over_img_rect)
#
pygame.display.update()
#
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()




















