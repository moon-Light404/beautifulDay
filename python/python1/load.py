#coding:utf-8
from honor import *
import pickle
import re
#保存文件
def saveObj(obj,filename):
    f = open(filename+'.txt','wb')
    pickle.dump(obj,f)
    f.close()

#大Boss
Boss1 = FBoss()
Boss2 = ElectricFish()
Boss3 = Terminator()


try:
    f = open('weapon.txt', 'rb')
    manger = Manger()
    manger = pickle.load(f)
    f.close()

except:
    #添加两个武器
    w1 = Weapon('小刀', 20, 30, 0, 0,5)
    w2 = Weapon('木棍', 15, 20, 0, 0,5)
    #以下武器为我运行程序后手动添加
    weapon_total = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11]

    manger = Manger()
    # manger.weapon_Shop.append(w1)
    # manger.weapon_Shop.append(w2)
    for i in weapon_total:
        manger.weapon_Shop.append(i)
    saveObj(manger,'weapon')
#函数块
#-----------------------------------------------------




#添加装备管理员界面
def Mlogin(manger):
    while True:
        n = input('请输入你的选项操作:1.添加武器\t 2.删除武器\t3.查看所有玩家信息\t4.查看商店武器\t5.保存修改()记得保村，不然数据会偷偷溜走哦-----<-->\t6.退出返回')
        if n == '1':
            for i in manger.weapon_Shop:
                print(i)
            # w_num = int(input('-------请输入你要购买的武器编号------'))
            # your_weapon = manger.weapons[w_num+1]
            try:
                print('请输入武器属性:')
                name = input('输入名字')
                agg = int(input('输入攻击力'))
                price = int(input('输入价格'))
                hp = int(input('输入增加血量属性:'))
                rank = int(input('输入适用等级'))
                armor = int(input('输入护甲值'))
                new_w = Weapon(name,agg,price,hp,rank,armor)
            except:
                print('老师请你用整数输入价格等属性哦----->>>>')
            #添加装备到商店库存中\
            else:
                if manger.Add_weapons(new_w):
                    print('恭喜俊哥添加装备成功!')
                else:
                    print('装备已经存在！！')
        elif n == '2':
            weapon_name = input('请输入要删除武器的名字')
            if manger.del_weapons(weapon_name):
                print('恭喜丁俊大大删除装备成功，继续加油哦！')
            else:
                print('商店里还没有该装备哦！')

        elif n == '3':
            for p in person_list:
                #这里只能查看账户信息，英雄信息下次完善---
                print(p)
        elif n == '4':
            for weapon in manger.weapon_Shop:
                print(weapon)
        elif n=='5':#保存武器信息
            saveObj(manger,'weapon')
            print('保存成功!!!')
        elif n == '6':
            break


#1、时空裂隙战斗
def space_fight(player,Role):#和普通怪兽打斗
    print('------你正在进入时空裂隙')
    _hp = Role.hp
    _mp = Role.mp
    #时空裂隙的怪兽
    m1 = Monster('地狱魔兽', 200, money=100, attack=120)
    m2 = Monster('邱小飞', 320, money=150, attack=125)
    m3 = Monster('黄哥哥',250,money=130,attack=100)
    m6 = Monster('老妖蛇',exp=200,hp=600,money=200,attack=150)
    m4 = Monster('月球机器',exp=210,hp=700,money=250,attack=180)
    m5 = Monster('河蟹',500,exp = 200,money = 400,attack = 400)
    while True:

        Mon_list = [m1, m2, m3,m4,m5,m6]
        the_mon = choice(Mon_list)
        m_hp = the_mon.hp
        print(Role)
        print(the_mon)
        fight_round = 1
        while Role.alive and the_mon.m_isAlive():
            print('----第%02d回合--------' % fight_round)
            print('%s对%s使用了%s,造成了%d的伤害' % (the_mon.name, Role.name, the_mon.skill, the_mon.Fir_attack(Role)))
            cho = input('请输入你释放的技能选项(输入其他就逃跑):1.%s\t2.%s\t3.%s\t4.%s' % (Role.skills[0], Role.skills[1], Role.skills[2],Role.skills[3]))
            if cho == '1':
                print('%s对%s使用了%s,造成了%d伤害' % (Role.name, the_mon.name, Role.skills[0], Role.common_Attack(the_mon)))
            elif cho == '2':
                if Role.small_Attack(the_mon):
                    print('%s对%s使用了%s' % (Role.name, the_mon.name, Role.skills[1]))
                else:
                    print('%s对%s使用了%s,造成了%d伤害' % (Role.name, the_mon.name, Role.skills[0], Role.common_Attack(the_mon)))
            elif cho == '3':
                if Role.big_Attack(the_mon):
                    print('%s对%s使用了%s' % (Role.name, the_mon.name, Role.skills[2]))
                    re_hp,re_mp = Role.resume()
                    print('%s使用大招后回复了%d点血量,%d点蓝量'%(Role.name,re_hp,re_mp))
                else:
                    print('蓝量不足_释放技能失败')
            elif cho == '4':
                Role.back_hp(_hp,_mp)
                print('你使用了回复又满状态了----')
            else:
                print('-----逃跑成功----')
                break
            display_info(Role, the_mon)
            fight_round += 1
            time.sleep(2)
        #循环结束判断升级已经血量处理
        if Role.alive:
            c = input('是否回复血量值:1.Yes 2.NO')
            if c == '1':
                Role.back_hp(_hp,_mp)
            else:
                print('战斗要小心哦----')
            Role.hero_add_exp(the_mon)
            print('%s成功打败了%s,获得了%d金币,%d经验' % (Role.name, the_mon.name, the_mon.money, the_mon.exp))
            the_weapon = choice(drop_weapon)
            for i in Role.weapons:
                if i.w_name == the_weapon.w_name:
                    print('怪兽掉落了一件%s,但是很遗憾背包中已经有了'%the_weapon.w_name)
                    break
            else:
                Role.Get_weapon(the_weapon)
                print('你得到了一件%s'%the_weapon.w_name)
            if Role.hero_IsRank():
                print('等级提升')
            else:
                pass

            print(Role)

        else:
            print('你被打死了!')
            print('别灰心，去努刷副本升级得装备和经验吧努力变得更强!加油----')
            print('----正在回复血量和mp中.会消耗一定金币哦，不然你无法站起来和小喵一起战斗了')
            Role.back_hp(_hp,_mp)
            print('回复成功！你又能站起来了!!!')
        the_mon.back_hp(m_hp)#怪兽回复血量
        num = input('是否继续战斗 1.Yes  2.NO-------')
        if num == '1':
            pass
        else:#随便输入什么都是退出循环
            break #退出时空裂隙，退出战斗




#--------------------------------------------------------------------------------------------------









        # num = input('是否继续战斗----1.是  2.否')
        # if num == '1':
        #     ch = input('是否花钱回复血量和HP----1.是   2.否')
        # else:
        #     flag = True





#判断用户账号格式是否正确
def is_vaild_uname(uName):
    ex_uname = re.compile(r'^[1-9][0-9]{4,10}[a-zA-Z]{3}$')
    result = ex_uname.match(uName)
    if result:
        return True
    else:
        return False
#测试点
# name = input()
# print(is_vaild_uname((name)))


#-------------------------------------------------------------
#玩家选择职业英雄
def cho_Hero(cho,player):
    return {
        '1': player.Heros[0],
        '2': player.Heros[1],
        '3': player.Heros[2],
        '4': 'exit'
    }.get(cho, 'non')
#随机从怪兽群中挑选怪兽
def cho_Monster(cho):
    return{
        '1':Boss1,
        '2':Boss2,
        '3':Boss3,
    }.get(cho,'non')
def isWin(hero):
    for flag in hero.wins.values():
        if flag == 0:
            return False
    return True  #全打败了
#角色打工赚钱方法
def add_money(role):
    i = 1
    while True:
        print('---------------打工赚钱中------------')
        i += 1
        time.sleep(3)
        role.money += 20
        print('你赚了20金币!')
        if i == 5:
            break
#检查要买的装备是否已经存在背包里面并购买装备
def check_weapons(hero,buy_weapon):
    for i in hero.weapons:
        if i.w_name == buy_weapon.w_name:
            return False
    hero.Buy_weapon(buy_weapon)
    return True
#--------------------------------------------------------------
#角色确定进入游戏画面选项
def player_in(i,role):#i是玩家 player  role 是选择的职业角色---参数----
    print('欢迎')
    while True:
        cho = input('请输入选项:1.时空裂隙(升级)\t2.混沌之战(Boss)\t3.商店\t4.充值\t5.退出游戏\t6.查看当前角色信息\t 7.返回\t8.存档(记得哦，~~不然数据会丢失哦~~)\t9.打工赚钱')
        if cho == '1':#进入时空裂隙
            space_fight(i,role)
        elif cho == '2':#进入混沌之战单挑boss
            # boss_num = cho_Monster(input('请选择你要挑战的怪兽'))
            # if Boss
            #
            #先打败第一只怪兽
            if role.rank < 5:
                print('你现在太弱了还没到五级，快去变得更强!')
            if  not isWin(role):#还没有通关所有副本
                if role.rank >= 5 and not role.wins['枉死之身']:
                    fight_Devils(role,Boss1)
                elif role.rank < 10 and role.wins['枉死之身']:
                    print('等级还不够,请到达十级以后来挑战')
                    #先判断是否能不能打大Boss
                elif role.rank > 20 and role.wins['电气八爪鱼']:
                    fight_Devils(role,Boss3)
                elif role.rank >= 10 and role.wins['枉死之身']:
                    fight_Devils(role,Boss2)


            elif isWin(role):
                print('恭喜你已经集齐了三大Boss勋章，现在可以自由单挑了')
                the_Boss = cho_Monster(input('请选择你要挑战的怪兽1\t 2\t 3\t'))
                if the_Boss == 'non':
                    print('输入选项错误')
                else:
                    fight_Devils(role,the_Boss)

        elif cho == '3':#商店购买装备----
            newcho = input('请输入选项1.购买装备\t 2.出售装备\t')
            if newcho == '1':
                sort_w = 1
                for i in manger.weapon_Shop:
                    print(f'{sort_w}:{i}')
                    sort_w += 1
                try:
                    m = int(input('请输入你要购买的武器选项编号:'))
                except:
                    print('请输入整数')
                else:
                    try:
                        pre_weapon = manger.weapon_Shop[m-1]
                    except:
                        print('武器不存在!!!')
                    else:
                        if role.Is_can_Buy(pre_weapon ) and check_weapons(role,pre_weapon):#武器不在英雄的装备库里
                            print(f'恭喜你购买{pre_weapon.w_name}成功.增加了{pre_weapon.w_aggressive}点攻击力！')
                        else:
                            print('还不能购买此装备,可能背包里面有了,也许可能是等级不够哦,努力升级和赚钱吧!')
            elif newcho == '2':
                if not role.weapons:
                    print('背包里还没有武器')
                else:
                    sort_w = 1
                    for i in role.weapons:
                        print(f'{sort_w}:{i}')
                        sort_w += 1
                    try:
                        sell_w = int(input('请输入你要出售的武器选项:'))
                    except:
                        print('请输入整数!')
                    else:
                        try:
                            pre_weapon = role.weapons[sell_w-1]
                        except:
                            print('武器不存在!!!')
                        else:
                            if not check_weapons(role,pre_weapon):#在背包中找到了这件武器
                                role.Sell_weapon(pre_weapon)
                                print(f'恭喜你出售{pre_weapon.w_name}成功.获得了{pre_weapon.w_price}金币')




        elif cho == '4':

            try:
                re_money = int(input('请输入你要充值的金币:'))
            except:
                print('输入格式错误')
            else:
                if i.Recharge(role,re_money):
                    print('充值成功!本次充值%d金币,银行卡剩余金币%d金币'%(re_money,i.bank_money))
                else:
                    print('钱不够了---<>')

        elif cho == '5':
            exit()


        elif cho == '6':
            zd = 1
            print(role)
            print('你的武器有:')
            for i in role.weapons:
                print(f'{zd}.{i}')
                zd += 1
        elif cho == '7':
            break


        elif cho == '8':
            saveObj(person_list,'load')
            print('存档成功!你又偷偷变强了----')
        elif cho == '9':
            add_money(role)

#-------------- -----------------------------------------------------------------



def Ulogin(i):
    while True:
        cho = cho_Hero(input('请选择你的角色:1.天剑通灵\t 2.红莲之刃\t 3.无影枪炮\t(---输入4退出选项返回上一级---谢谢!!!)'),i)
        if cho == 'non':
            print('英雄选项不存在!')
        elif cho == 'exit':
            break
        else:
            your_hero = cho
            print('-'*40)
            print('--------欢饮来到机甲旋风------')
            print(your_hero)
            print('-' * 40)
            player_in(i,your_hero)






#-----------------------------------------------------------------------------------
try:
    f = open('load.txt', 'rb')
    person_list = pickle.load(f) #存放用户登录信息的列表,里面每一个元素都是一个对象userload
    f.close()
except:
    p = Person('内测玩家','198328781abc','147258')#手动添加一个账户
    person_list = []
    person_list.append(p)
    f = open('load.txt', 'wb')
    pickle.dump(person_list,f)
    f.close()
#-------------------------------------------------------------------------------------
def main():
    print('-'*50)
    print('===============版权信息===============')
    print('              作者：丁俊               ')
    print('             班级:信安193班           ')
    print('           作品:机甲旋风怀旧模拟器         ')
    print('管理员登录账户：1908328781\t 147258690adc')
    print('如果需要测试高等级请登录账号 198328781abc \t 147258')
    print('='*40)
    while True:
        choi = input('请输入你的选项:1.登录游戏\t 2.注册账号\t 3.查看背景信息\t4、管理员登录\t5.退出游戏')
        if choi == '1':#用户登录
            uName = input('请输入你的账号:')
            password = input('请输入你的密码:')
            flag = True
            for i in person_list:#i是个用户对象
                if uName == i.name:
                    if password == i.key_word:
                        print('登录成功!')
                        flag = False
                        Ulogin(i)#进入用户选择角色界面-----
                    else:
                        flag = False
                        print('密码错误')
            if flag == True:
                print('账号输入错误!')


            # try:
            #     if uName not in userLoad:
            #         raise Exception('账号不存在')
            #     elif userLoad[uName] != password:
            #         raise Exception('密码错误!')
            #     else:
            #         print('登录成功!')
            #         # Ulogin()#用户登录成功界面
            # except Exception as e:
            #     print(e)


        elif choi == '2':#注册
            times = 0
            while True and times <3:#设置注册次数
                uName = input('请输入要注册的账号(6-11位数字 + 三个英文字母,不区分大小写):')
                if is_vaild_uname(uName):
                    for i in person_list:
                        if i.name == uName:
                            print('该账号已经被注册过,请输入一个新的账号——————')
                            break       #账号重复终止输入循环，重新输入账号
                    else:#没有找到重复的账号，输入密码注册成功！
                        password = input('请输入你的密码:')
                        nick = input('离成功还差一步，请输入你的游戏昵称吧!')
                        p1 = Person(nick,uName,password)
                        person_list.append(p1)#添加到玩家列表中
                        saveObj(person_list,'load')
                        print('注册成功,快去登录吧!!!')
                        break

                else:
                    print('格式错误!')
                    times +=1
        elif choi == '3':
            print('马丁博士致力于研究怪兽变异碎片的研究，派遣机器战士挑战怪兽，征战于怪兽巢穴------')

        elif choi == '4':  # 管理员登录
            mangerName = input('请输入管理员账号:')
            if mangerName == manger.account:
                mangerWord = input('请输入管理员密码:')
                if mangerWord == manger.code:
                    print('登录管理员成功!!!')
                    Mlogin(manger)#进入管理员界面
                else:
                    print('密码错误——————')
            else:
                print('管理员账号错误——————')
        elif choi == '5':
            print('-'*50)
            print('欢迎下次来到机甲旋风')
            exit()
main()



