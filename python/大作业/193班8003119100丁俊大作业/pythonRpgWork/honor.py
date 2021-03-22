#coding:utf-8
from abc import ABCMeta,abstractmethod
from random import randint,uniform,choice
import pickle
import time
#------------------------------------------------------------
#武器类
class Weapon(object):#武器类的属性以         w_开头 我把与武器有关的方法放在了武器类中
    __slots__ = ('w_name','w_aggressive','w_price','w_hp','w_rank','w_armor')
    def __init__(self,name,aggressive,price,hp,rank,armor):
        self.w_name = name
        self.w_aggressive = aggressive
        self.w_price = price
        self.w_hp = hp
        self.w_rank = rank
        self.w_armor = armor


    def __str__(self):
        return '%s\t'%self.w_name+\
      '攻击力:%d\t' %self.w_aggressive+\
        '价格:%d\t' %self.w_price+\
        '适用等级:%d\t' %self.w_rank

#----------------------------------------------------
w1 = Weapon('小刀', 20, 30, 0, 0,5)
w2 = Weapon('木棍', 15, 40, 0, 0,5)
w3 = Weapon('怪兽之刃',15,45,0,0,5)

drop_weapon = [w1,w2,w3]

w3 = Weapon('暴风雪', 100, 150, 200, 5, 50)
w4 = Weapon('冰风', 200, 300, 250, 8, 100)
w5 = Weapon('雷电', 300, 450, 300, 9, 140)
w6 = Weapon('彩虹刀', 800, 2500, 600, 15, 180)
w7 = Weapon('稀有GFX9型光炮', 1500, 1000, 1100, 15, 240)
w8 = Weapon('时空天剑引擎', 1200, 1800, 1500, 15, 250)
w9= Weapon('传奇cpu', 2000, 2800, 1800, 20, 280)
w11 = Weapon('魔杖',2200,100000,2000,15,320)
w10 = Weapon('终结权杖',2500,100000,3000,20,450)#不可以买只能打boss获得,
#---------------------------------------------------------------------------
class hero(object,metaclass= ABCMeta):#英雄基类
    # __slots__  = ('name','hp','money','rank','mp','exp','attack','armor')
    def __init__(self,name,hp,money,rank,exp,mp,armor,attack):
        self.name = name
        self.hp = hp
        self.money = money
        self.mp = mp
        self.armor = armor
        self.attack = attack
        self.exp = exp
        self.rank = rank#八个属性
        self.weapons = []#存放武器对象
        self.wins = {'枉死之身':0,'电气八爪鱼':0,'结合体莫卡伊':0}

   #英雄死亡之后血量为0,退出打怪模式，后回复上次血量,钱减100
    def back_hp(self,hp,mp):
        self.hp = hp
        self.mp = mp
        self.money -= 100
    @property
    def alive(self):
        return  self.hp > 0

    def resume(self):#回复状态
        """
        回复魔法值
        :return: 喝药之后回复的魔法值
        """
        incr_point = self.mp // 4
        self.mp += incr_point
        hp_point =  self.hp // 8
        self.hp += hp_point
        return incr_point,hp_point
    #判断是否升级
    def hero_IsRank(self):
        #200经验值一级
        new_rank= self.exp // 200
        add_rank = new_rank - self.rank#升级的级数
        if add_rank > 0:
            self.rank += add_rank
            self.hp += 150*add_rank
            self.mp += 30*add_rank  #升级加血量和蓝值,攻击和防御属性升级!!!
            self.attack += 100*add_rank
            self.armor += 25*add_rank
            return True#判断是否升级
        else:
            return False

    def hero_add_exp(self,other): #打败其他怪兽获得经验
        self.exp += other.exp
        self.money += other.money
         #返回获得的经验值,然后判断是否升级
    def __str__(self):
        return '~~~%s~~~~\t' % self.name + \
               '生命值: %d\t' % self.hp + \
               '魔法值:%d\t' % self.mp + \
               '当前金币: %d\t' % self.money + \
               '当前等级: %d\t' % self.rank + \
               '当前伤害:%d\t' % self.attack+\
                '当前护甲%d' %self.armor
    def Buy_weapon(self,weapon):#买装备
        if self.money > weapon.w_price:
            self.weapons.append(weapon)#添加自己的武器到背包中
            self.money -= weapon.w_price
            self.attack += weapon.w_aggressive
            self.hp += weapon.w_hp#交易金钱和...
            self.armor += weapon.w_armor
            return True
        else:
            return False

    def Sell_weapon(self,weapon):#卖装备
        self.weapons.remove(weapon)#移除装备获得金钱
        self.money += weapon.w_price
        self.attack -= weapon.w_aggressive
        self.hp -= weapon.w_hp
        self.armor -= weapon.w_armor
    def Get_weapon(self,weapon):
        self.weapons.append(weapon)
        self.attack += weapon.w_aggressive
        self.hp += weapon.w_hp
        self.armor += weapon.w_armor
    def Is_can_Buy(self, w):# 参数是准备要购买的武器
        if self.rank >= w.w_rank and  self.money >= w.w_price:#钱和等级都够了才能购买---
            return True
        else:
            return False

    @abstractmethod#虚方法,让下面的子类进行完善
    def common_Attack(self,other):
        """
        攻击
        :param other: 被攻击对象
        :return:
        """

        pass



#------------------------------------------------------------------------------
class SkySprit(hero):
    """
    天剑通灵
    """
    # __slots__ = ('name', 'hp', 'money', 'rank', 'mp', 'exp', 'attack', 'armor')

    def __init__(self,name='天剑通灵',hp = 1000,money=1000,rank=0,exp=0,mp=500,armor =30,attack=75):
        super().__init__(name,hp,money,rank,exp,mp,armor,attack)
        self.skills = ['不畏刺击', '怒气爆发','冰霜磁场','回复']

    def common_Attack(self,other):
        """
        普通攻击
        :param other: 敌人
        :return: 随机伤害
        """

        damage_Value = self.attack - other.armor
        other.hp -= damage_Value
        return damage_Value

    def small_Attack(self,other): #一技能
        if self.mp > 300:
            self.mp -= 300
            damage_value = randint(1,2)*self.attack +randint(0,250)- other.armor
            other.hp -= damage_value
            return True
        else:
            return False

    def big_Attack(self,other):#二技能
        if self.mp > 400:
            self.mp -= 400
            damage_value = randint(2,3)*self.attack+ randint(0,500) - other.armor
            other.hp -= damage_value
            return True
        else:
            return False
#---------------------------------------------------------------------------------------------------
class RedLotus(hero):
    """
   红莲之忍英雄
    """

    __slots__  = ('name','hp','money','rank','mp','exp','attack','armor')

    def __init__(self,name='红莲之刃',hp = 900,money=1000,rank=0,exp=0,mp=400,armor =30,attack=80):
        super().__init__(name,hp,money,rank,exp,mp,armor,attack)
        self.skills = ['背后利刃', '风火轮', '天莲炫冲','回复']

    def common_Attack(self,other):
        """
        普通攻击
        :param other: 敌人
        :return: 随机伤害
        """
        damage_Value = self.attack - other.armor
        if damage_Value > 0:
            other.hp -= damage_Value
            return damage_Value
        else:
            return 0

    def small_Attack(self,other):
        if self.mp > 200:
            self.mp -= 200
            damage_value = randint(1,2) * self.attack - other.armor
            other.hp -= damage_value
            return True
        else:
            return False

    def big_Attack(self,other):
        if self.mp > 400:
            self.mp -= 400
            damage_value = 3*self.attack + randint(0,500) - other.armor
            other.hp -= damage_value
            return True
        else:
            return False
#-----------------------------------------------------------------------------------------------
class EkGunman(hero):#无影枪炮
    """
    无影枪炮英雄
    """
    __slots__ = ('name', 'hp', 'money', 'rank', 'mp', 'exp', 'attack', 'armor')

    def __init__(self, name='无影枪炮', hp=1200, money=1000, rank=0, exp=0, mp=600, armor=30, attack=70):
        super().__init__(name, hp, money, rank, exp, mp, armor, attack)
        self.skills = ['蜜汁炮弹', '激光炮', '离子机枪','回复']

    def common_Attack(self, other):
        """
        普通攻击
        :param other: 敌人
        :return: 随机伤害
        """
        damage_Value = self.attack - other.armor
        if damage_Value > 0:
            other.hp -= damage_Value
            return damage_Value
        else:
            return 0

    def small_Attack(self, other):
        if self.mp > 200:
            self.mp -= 200
            damage_value = 2 * self.attack - other.armor
            other.hp -= damage_value
            return True
        else:
            return False

    def big_Attack(self, other):
        if self.mp > 400:
            self.mp -= 400
            damage_value = 2.5 * self.attack + randint(0, 500) - other.armor
            other.hp -= damage_value
            return True
        else:
            return False

#-----------------------------------------------------------------------------------------------
class Monster(object):#怪兽基类
    __slots__ = ('name','hp','exp','money','attack','skill','armor')
    def __init__(self,name,hp=300,exp=100,money=120,attack = 100,armor = 0):
        self.name = name
        self.hp = hp
        self.exp = exp
        self.money = money
        self.attack = attack
        self.armor = armor
        self.skill = '打击'
    def m_isAlive(self):#判断怪兽是否活着
        if self.hp > 0:
            return True
        else:
            return False

    def Fir_attack(self, hero):
        # 攻击英雄，对其造成伤害
        damage_Value = randint(1,2)*self.attack - hero.armor
        if damage_Value > 0:
            hero.hp -= damage_Value
            return damage_Value
        else:
            return 0
    def back_hp(self,hp):
        self.hp = hp
    def __str__(self):
        return '名字:%s\t'%self.name+\
            '怪兽血量:%d\t'%self.hp +\
    '怪兽金币:%d\t'%self.money+\
    '怪兽经验:%d'%self.exp
#-----------------------------------------------------------------------------------
class FBoss(Monster):#怪兽BOSS1

    def __init__(self,name='枉死之身',hp=3500,exp=600,money=1000,attack= 300,armor=100):
        super().__init__(name,hp,exp,money,attack,armor)
        self.final_str = return_str('Boss1')
        self.mskills = ['打击','烈火咆哮','烈焰烧身','自杀']
        self.weapons = [w1,w2,w3,w4,w5,w6]
    def Sec_attack(self, hero):
        damage_Value =  self.attack + randint(300,600) - hero.armor
        if damage_Value > 0:
            hero.hp -= damage_Value
            return damage_Value
        else:
            return 0
    def Thr_attack(self,hero):
        damage_value = 3*self.attack +randint(300,1000) - hero.armor
        if damage_value > 0:
            hero.hp -= damage_value
            return damage_value
        else:
            return 0

    def commit_attack(self,hero):
        damage = self.hp // (1.5)
        hero.hp -= damage #Boss自杀，造成巨大伤害
        self.hp = 0
        return damage #伤害

def return_str(filename):
    f = open(filename+ '.txt','r',encoding='utf-8')
    s = f.read()
    f.close()
    return s
class ElectricFish(Monster):
    """
    电气八爪鱼#固定伤害输出
    """

    def __init__(self,name='电气八爪鱼',hp=6000,exp=1200,money=1800,attack=500,armor=180):
        super().__init__(name,hp,exp,money,attack,armor)
        self.mskills = ['压倒','暗之光芒','电闪雷鸣','魔电翻涌']
        self.weapons = [w1,w2,w3,w4,w6,w7]
        self.final_str = return_str('Boss2')
    def Sec_attack(self, hero):
        damage_Value =  randint(2,3)*self.attack + randint(300,1000) - hero.armor
        if damage_Value > 0:
            hero.hp -= damage_Value
            return damage_Value
        else:
            return 0
    def Thr_attack(self,hero):
        damage_value = randint(3,4)*self.attack + randint(400,1400) - hero.armor
        if damage_value > 0:
            hero.hp -= damage_value
            return damage_value
        else:
            return 0

    def commit_attack(self,hero):
        damage = 4000
        hero.hp -= 4000
        return damage
#-----测试字符串
# e1 = electricFish()
# print(e1.final_str)
#-------------------


class Terminator(Monster):
    def __init__(self,name='结合体莫卡伊',hp=15000,exp=2300,money=3000,attack=1250,armor=500):
        super().__init__(name,hp,exp,money,attack,armor)
        self.final_str = return_str('Boss3')
        self.mskills = ['麻痹','无双触手','分身怒吼','六子箴言咒']
        self.weapons = [w3,w4,w5,w6,w7,w8,w9,w10,w11]
    def Sec_attack(self, hero):
        damage_Value =  hero.hp // randint(3,4) - hero.armor
        if damage_Value > 0:
            hero.hp -= damage_Value
            return damage_Value
        else:
            return 0
    def Thr_attack(self,hero):
        damage_value = hero.hp // 3 - hero.armor
        if damage_value > 0:
            hero.hp -= damage_value
            return damage_value
        else:
            return 0

    def commit_attack(self,hero):
        damage_value = 8000
        hero.hp -=  damage_value
        return  damage_value
#--------------------------------------------------------------
#用户类

T = SkySprit()
R = RedLotus()
E = EkGunman()
# T.exp = 550
# print(T.hero_IsRank())
# print(T)
class Person():
    __slots__ = ('nickname','name','key_word','bank_money','Heros')

    def __init__(self,nick,name,word,money= 4000,):#参数有初始值就不要传参数
        self.nickname = nick
        self.name = name
        self.key_word = word
        self.bank_money = money#每个人特定银行卡有2000元，与个人账号绑定在一起
        self.Heros = [T,R,E]
    #为英雄充值金币用于购买装备
    def Recharge(self,hero,add_money):
        if self.bank_money > add_money:
            self.bank_money -= add_money
            hero.money += add_money
            return True
        else:
            return False


    def __str__(self):
        return '账号:%s\n' % self.name+\
    '密码%s\n' % self.key_word +\
    '玩家昵称:%s\n'%self.nickname+\
    '银行卡余额:%d\n'%self.bank_money
# p = Person('190832v','小飞','147258')
# for i in p.Heros:
#     print(i)
# person_list = []
# person_list.append(p)

# p1 = Person('1908ab','小康','147852')
# person_list.append(p1)
# for i in person_list:
#     print(i)
#----------------------------------------------------------------------------------
#显示敌人和英雄信息
def display_info(player,enemy):
    print(player)
    print(enemy)

#敌人随机发动技能:
def Enemy_attack(monster,other):
    rand_num = randint(1,100)
    if rand_num >= 90:#发动大招commit_attack
        print('%s对%s使用%s造成了%d点伤害' % (monster.name, other.name,monster.mskills[3],monster.commit_attack(other)))
    elif rand_num >= 80: #Thr_attack
        print('%s对%s使用了%s造成了%d点伤害' % (monster.name, other.name,monster.mskills[2],monster.Thr_attack(other)))
    elif rand_num >= 40:#Sec_attack
        print('%s对%s使用了%s造成了%d点伤害' %(monster.name,other.name,monster.mskills[1],monster.Sec_attack(other)))
    else:
        print('%s对%s使用了%s造成了%d点伤害' % (monster.name, other.name, monster.mskills[0], monster.Fir_attack(other)))
#--------------------------------------------------------------------------------

def fight_Devils(Role,Boss):#与boss对战
    #先记录各自的血量,以便战斗结束后回复血量
    _hp = Role.hp
    _mp = Role.mp
    Hp = Boss.hp
    while True:
        display_info(Role, Boss)
        fight_round = 1#---记录轮数---

        while Role.alive and Boss.m_isAlive():
            print('----第%02d回合--------' % fight_round)
            cho = input('请输入你释放的技能选项(输入其他就逃跑):1.%s\t2.%s\t3.%s\t4.%s' % (Role.skills[0], Role.skills[1], Role.skills[2],Role.skills[3]))
            if cho == '1':
                print('%s对%s使用了%s,造成了%d伤害' % (Role.name, Boss.name, Role.skills[0], Role.common_Attack(Boss)))
            elif cho == '2':
                if Role.small_Attack(Boss):
                    print('%s对%s使用了%s' % (Role.name,Boss.name, Role.skills[1]))
                else:
                    hurt = Role.common_Attack(Boss)
                    print('%s对%s使用了%s,造成了%d伤害' % (Role.name, Boss.name, Role.skills[0], hurt))
            elif cho == '3':
                if Role.big_Attack(Boss):
                    print('%s对%s使用了%s' % (Role.name, Boss.name, Role.skills[2]))
                    re_hp, re_mp = Role.resume()
                    print('%s使用大招后回复了%d点血量,%d点蓝量' % (Role.name,re_hp, re_mp))
                else:
                    print('蓝量不足_释放技能失败')
            elif cho == '4':
                Role.back_hp(_hp,_mp)
                print('你使用了回复满状态了!')
            else:
                print('-----逃跑成功-----')
                break
            Enemy_attack(Boss,Role)
            display_info(Role, Boss)
            fight_round += 1
            time.sleep(2)
        if Role.alive:
            c = input('是否回复血量值:1.Yes 2.NO')
            if c == '1':
                Role.back_hp(_hp, _mp)
            else:
                print('没加血要更加小心战斗哦!!')
            Role.hero_add_exp(Boss)
            Role.wins[Boss.name] = 1#标志获得勋章，打败了这只怪兽
            print('%s成功打败了%s,获得了%d金币,%d经验,获得了%s勋章' % (Role.name, Boss.name, Boss.money, Boss.exp,Boss.name))
            print(Boss.final_str)
            the_weapon = choice(Boss.weapons)
            for i in Role.weapons:
                if i.w_name == the_weapon.w_name:
                    print('怪兽掉落了一件%s,但是很遗憾背包中已经有了' % the_weapon.w_name)
                    break
            else:
                Role.Get_weapon(the_weapon)
                print('你得到了一件%s' % the_weapon.w_name)

            if Role.hero_IsRank():
                print('等级提升')
            else:
                pass

            print(Role)

        else:
            print('你被打死了!')
            print('别灰心，去努刷副本升级得装备和经验吧努力变得更强!加油----')
            print('----正在回复血量和mp中.会消耗一定金币哦，不然你无法站起来和小喵一起战斗了')
            Role.back_hp(_hp, _mp)
            print('回复成功！你又能站起来了!!!')
        Boss.back_hp(Hp) #Boss恢复血量
        num = input('是否继续战斗 1.Yes  2.NO-------')
        if num == '1':
            pass
        else:
            break  # 退出混沌之战，退出战斗


# T1 = SkySprit(hp=10000,money=1000,rank = 100,exp=20000,mp=3000,armor=400,attack = 2000)
#
# boss = Terminator()
# fight_Devils(T1,boss)
#-----------------
class Manger(object):
    def __init__(self,account = '1908328781',code='1472583690adc'):
        self.account = account
        self.code = code
        self.weapon_Shop = []

    def mange_weapon(self,add_weapon):#add_weapon要增加的武器对象
        self.weapon_Shop.append(add_weapon)
    #为商店添加
    def Add_weapons(self,newweapon):
        for i in self.weapon_Shop:
            if i.w_name == newweapon.w_name:#武器名字重复
                return False
        #前面没有找到重复的武器------>添加武器成功
        self.weapon_Shop.append(newweapon)
        return True
    #商店交货
    def del_weapons(self,del_name):#del_name要删除武器的名字
        for i in self.weapon_Shop:
            if i.w_name == del_name:
                self.weapon_Shop.remove(i)#找到了相同的武器名字移除
                return True
        return False