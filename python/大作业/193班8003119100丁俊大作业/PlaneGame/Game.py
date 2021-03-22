# coding:utf-8
from pygame.locals import *
from GameObj import *
import os, sys
import time
import random



# 初始化游戏
pygame.init()
# 创建一个屏幕   set_mode((width,height))
screen = pygame.display.set_mode((480, 700))
# 设置标题
pygame.display.set_caption('打飞机游戏')
# 载入背景图片  pygame.image.load直接读取图片
background_img = pygame.image.load('data\\img\\background.png')
# 得到相关的矩形参数
background_img_rect = background_img.get_rect()
# 载入游戏结束的背景图片
game_over_img = pygame.image.load('data\\img\\gameover.png')
# 得到相关的矩形参数
game_over_img_rect = game_over_img.get_rect()
# 载入shoot大图
shoot = pygame.image.load('data\\img\\shoot.png')
# 载入音效    pygame.mixer.music.load直接运行
game_music_sound = pygame.mixer.music.load('data\\audio\\game_music.wav')
# 初始化音乐相关参数    play(loops=0 -1表示一直重复,start=0,秒数)
pygame.mixer.music.play(-1, 0.0)
# 设置音量   0-1  1最大
pygame.mixer.music.set_volume(0.5)
# 玩家飞机在shoot中的位置列表
hero_rects = []
hero_recten = []
# pygame.Rect(left,top,width,height)
hero_rects.append(pygame.Rect(0, 100, 105, 130))  #
hero_rects.append(pygame.Rect(175, 245, 105, 130))  # 被击中时的敌机
hero_pos = [0, 500]  # 玩家飞机的初识位置

# 构造一个
hero = Hero(shoot, hero_rects, hero_pos)
# 得到子弹的图片
bullet_rect = pygame.Rect(1004, 987, 13, 24)
bullet_img = shoot.subsurface(bullet_rect)  # 得到子弹图片，还未画出来

# 敌方飞机
enemy1_rect = pygame.Rect(535, 620, 50, 36)
enemy1_img = shoot.subsurface(enemy1_rect)

enemy1_down_rect = pygame.Rect(270, 360, 50, 36)
enemy1_down_img = shoot.subsurface(enemy1_down_rect)
# 敌机的精灵组
enemies1_down = pygame.sprite.Group()
enemies1 = pygame.sprite.Group()


#Boss图片
Boss_rect = pygame.Rect(170,750,170,255)
Boss_img = shoot.subsurface(Boss_rect)
Boss_img=pygame.transform.smoothscale(Boss_img,(150,150))
#
Boss_down_rect = pygame.Rect(170,475,170,255)
Boss_down_img = shoot.subsurface(Boss_down_rect)
Boss_down_img = pygame.transform.smoothscale(Boss_down_img,(150,150))
#Boss精灵组
Boss_group = pygame.sprite.Group()
Boss_down_group = pygame.sprite.Group()


#炸弹
Beng_rect = pygame.Rect(105,118,60,110)
Beng_img = shoot.subsurface(Beng_rect)
Beng_group = pygame.sprite.Group()
Beng_down_rect=pygame.Rect(103,120,60,111)
Beng_down_img=shoot.subsurface(Beng_rect)
Beng_down_group=pygame.sprite.Group()

#用来标识炸弹是否存在
isBengExist = False

#标识符。用来标识是否有boss
isBossExist = False

wudi = False#无敌状态
shoot_times = 0  #我方战机子弹频率
score = 0  #分数


#h释放炸弹
def clear():
    for enemy1 in enemies1:
        enemies1_down.add(enemy1)
        enemies1.remove(enemy1)
    for boss in Boss_group:
        boss.HP=-1









enemies_times = 0
# 载入游戏结束的背景图片
game_over_img = pygame.image.load('data\\img\\gameover.png')
# 得到相关的矩形参数
game_over_img_rect = game_over_img.get_rect()

# 游戏开始的方法
running = True
while running:
    if score > 2000:
        break
    # 判断用户是否点击了关闭按钮:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # 系统的退出方法
    '''
            帧速率，是指程序每秒在屏幕中绘制图像的数目，用FPS来表示
            一般都能达到每秒60帧，越低越卡
    '''
    pygame.time.Clock().tick(60)

    # 绘制背景
    screen.fill(55)  # 设置屏幕的颜色  fill(RGB)
    # blit(背景图，位置)
    screen.blit(background_img, background_img_rect)


    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_SPACE]:
        if not hero.is_hit:
            if shoot_times == 5:
                hero.shoot(bullet_img)
            shoot_times += 1
            if shoot_times > 5:
                shoot_times = 0

    for bullet in hero.bullets:
        bullet.moveUp()
        if bullet.rect.top < 0:
            hero.bullets.remove(bullet)
    hero.bullets.draw(screen)
    # boss

    # 敌机
    if enemies_times % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_img, enemy1_pos)
        enemies1.add(enemy1)
    enemies_times += 1
    if enemies_times > 50:
        enemies_times = 0
    # 移动敌机
    for enemy1 in enemies1:
        enemy1.move()
        #敌机与战机相撞
        if pygame.sprite.collide_circle(enemy1, hero):
            enemies1_down.add(enemy1)
            enemies1.remove(enemy1)
            if not wudi:
                hero.is_hit = True
                break
        if enemy1.rect.top > SCREEN_HEIGHT:
            enemies1.remove(enemy1)
    collisions = pygame.sprite.groupcollide(enemies1, hero.bullets, True, True)
    for enemy1_down in collisions:
        enemies1_down.add(enemy1_down)
    #生成Boss
    if score % 200 == 0 and score > 0 and isBossExist == False:
        isBossExist = True
        #初始化一个boss
        Boss_pos = [180,0]
        boss = Enemy(Boss_img,Boss_down_img,Boss_pos)
        Boss_group.add(boss)
        #-------------------------------
    #生成炸弹
    if score % 250 == 0 and score > 0 and isBengExist == False:
        isBengExist = True
        Beng_pos = [random.randint(0, SCREEN_WIDTH - Beng_rect.width), 0]
        beng = Enemy(Beng_img, Beng_down_img, Beng_pos)#炸弹初始化
        Beng_group.add(beng)#添加炸弹消亡组


    for boss in Boss_group:
            #BOSS移动
        if boss.isMoveRight:
            boss.moveR()
        else:
            boss.moveL()
        boss.bullets.draw(screen)
        if enemies_times % 70 == 0:
            boss.shoot(bullet_img)
        #判断子弹是否击中飞机
        for bullet in boss.bullets:
            #两个精灵相撞
            bullet.moveDown()
            if bullet.rect.top > SCREEN_HEIGHT:
                boss.bullets.remove(bullet)
            if pygame.sprite.collide_circle(bullet,hero):
                boss.bullets.remove(bullet)
                hero.is_hit = True
                break
         #我方子弹与boss相遇问题
        for bullet in hero.bullets:
            if pygame.sprite.collide_circle(bullet,boss):
                hero.bullets.remove(bullet)
                boss.hp -= 10
                if boss.hp <= 0:
                    Boss_down_group.add(boss)
                    Boss_group.remove(boss)
                    isBossExist = False
        if pygame.sprite.collide_circle(boss, hero):
            boss.hp -= 50
            if boss.hp <= 0:
                Boss_down_group.add(boss)
                Boss_group.remove(boss)
                isBossExist = False
            hero.is_hit = True
            break
    for beng in Beng_group:
        beng.move()
        if pygame.sprite.collide_circle(beng, hero):
            hero.bengNum += 1
            Beng_down_group.add(beng)
            Beng_group.remove(beng)
            isBengExist = False

        #我方飞机与Boss相遇:

#---------------------------------------------------------------------------------------------

    #小飞机被击败的图片
    for enemy_down in enemies1_down:
        #击败组移除加分
        enemies1_down.remove(enemy_down)
        score += 10
        screen.blit(enemy_down.enemy_down_img,enemy_down.rect)
    #boos被击败的图片
    for boss_down in Boss_down_group:
        Boss_down_group.remove(boss_down)
        score += 50
        screen.blit(boss_down.enemy_down_img,boss_down.rect)

#-----------------------------------------------------------------------------------------------
    # for i in enemies1_down:  # 得分
    #     enemies1_down.remove(i)
    #     score += 10




    if not hero.is_hit:
        screen.blit(hero.image[0],hero.rect)
    else:
        screen.blit(hero.image[1],hero.rect)
        running=False

    # 绘制敌机
    enemies1.draw(screen)
    #绘制boss
    Boss_group.draw(screen)
    #画炸弹
    Beng_group.draw(screen)
    # 画分
    score_font = pygame.font.Font('data\\font\\CHILLER.TTF', 36)
    score_text = score_font.render(str(score), True, (240, 0, 87))
    score_text_rect = score_text.get_rect()
    screen.blit(score_text, score_text_rect)
    # 更新屏幕
    pygame.display.update()
    key_pressed = pygame.key.get_pressed()
    if not hero.is_hit:
        if key_pressed[K_UP] or key_pressed[K_w]:
            hero.moveUp()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            hero.moveDown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            hero.moveLeft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            hero.moveRight()
        if key_pressed[K_r]:#开启无敌模式
            wudi = True
        if key_pressed[K_b]:#关闭无敌模式
            wudi = False
        if key_pressed[K_h] and hero.bengNum >= 1: #清屏
            clear()
            hero.bengNum -= 1
screen.blit(game_over_img, game_over_img_rect)
# 游戏 Game Over 后显示最终得分
font = pygame.font.Font(None, 64)
text = font.render('Final Score: '+ str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over_img, (0, 0))
screen.blit(text, text_rect)

# 更新屏幕，屏幕内容有更改就要更新屏幕
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()