# coding:utf-8
from datetime import datetime
import pickle
import random


# 展示信息的方法
def show(uDic):
    print('你的名字是%s,当前等级%d,经验值%d,HP为%d' % (uDic['Name'], uDic['Lev'], uDic['Exp'], uDic['HP']))


# 判断是否升级的方法，在每次获得经验值时调用
def upLev(uDic):
    # 得到当前经验值应该达到的等级nu
    nu = int(uDic['Exp'] / 100)
    # 判断如果应该达到的等级>真实的等级则升级
    if nu > uDic['Lev']:
        print('恭喜你，升到了%d级,' % nu, end='')
        # random.randint(50,100) 得到随机整数，50、100都可以取到
        uDic['Lev'] = nu
        num = random.randint(50, 100)
        uDic['HP'] = uDic['HP'] + num
        print('HP回复%d' % num)


# 怪物攻击减少HP的方法，传入怪物可能造成的伤害作为参数
def monAttc(a, b, c):
    num = random.randint(1, 3)
    if num == 1:
        return a
    elif num == 2:
        return b
    else:
        return c


# 探险的方法(即遇怪物的方法)
def fight(uDic):
    # 随机生成1-100的一个整数，通过取值的范围来决定概率
    monster = random.randint(1, 100)
    # 大于90的数有10个，所以概率为10%
    if monster > 90:
        de = monAttc(50, 100, 150)
        print('菜虚鲲出现了，你受到了%d伤害！' % de)
        # 如果当前HP小于受到的伤害则被击败，HP降为0
        if uDic['HP'] <= de:
            print('你被菜虚鲲击败了！')
            uDic['HP'] = 0
        else:
            print('你击败了菜虚鲲，获得了250经验值，获得了300HP，强者的气息！')
            uDic['Exp'] += 250  # 得到经验值
            uDic['HP'] = uDic['HP'] + 300 - de  # 增加HP，但是要减去受到的伤害
            upLev(uDic)  # 判断是否会升级
    elif monster > 70:
        de = monAttc(30, 45, 50)
        print('狼人出现了，你受到了%d伤害！' % de)
        if uDic['HP'] <= de:
            print('你被狼人击败了！')
            uDic['HP'] = 0
        else:
            print('你击败了狼人，获得了80经验值，牛！')
            uDic['Exp'] += 80
            uDic['HP'] = uDic['HP'] - de
            upLev(uDic)
    else:
        de = monAttc(10, 15, 20)
        print('史莱克出现了，你受到了%d伤害！' % de)
        if uDic['HP'] <= de:
            print('你被史莱克击败了！')
            uDic['HP'] = 0
        else:
            print('你击败了史莱克，获得了30经验值，牛！')
            uDic['Exp'] += 80
            uDic['HP'] = uDic['HP'] - de
            upLev(uDic)


# 休息的方法
def sleepD(uDic):
    num = random.randint(10, 20)
    uDic['HP'] = uDic['HP'] + num
    print('得到休息，HP回复%d' % num)
    # 返回调用完休息方法的时间
    return datetime.now()


def login(uDic, uLi):
    show(uDic)
    isFir = True  # 如果是第一次休息，则不需要判断时间，用此标识符表示是否是第一次休息
    t1 = datetime.now()  # 定义一个t1变量，在调用休息的方法后，会返回一个新的值
    while True:
        cho = input('请输入你的操作:1.探险\t2.休息\t3.查看信息\t4.存档退出')
        if cho == '1':
            fight(uDic)
        elif cho == '2':
            # 调用方法时，定义t2变量，用此时的t2和调用休息方法后的t1求出时间差
            t2 = datetime.now()
            # 时间差大于10秒，或者是第一次调用休息的方法，可以调用
            if (t2 - t1).total_seconds() > 10 or isFir:
                isFir = False  # 第一次过后，此标识符变为False
                t1 = sleepD(uDic)  # 此方法返回调用完的时间t1,下一次调用时要用
            else:
                print('你休息的太频繁了！')
        elif cho == '3':
            show(uDic)
        else:
            f = open('user.txt', 'wb')
            pickle.dump(uLi, f)
            f.close()
            exit()  # 退出当前程序


# ------------主程序------------------
print('---欢迎来到勇者大冒险游戏---')
uLi = []  # 存放玩家信息的列表，玩家信息为字典，把所有玩家信息字典存入此列表，只需要序列化此列表即可！
uDic = {}
isNone = False  # 列表中是否有内容的标识符
try:
    f = open('user.txt', 'rb')
    uLi = pickle.load(f)
    print(uLi)
    f.close()
except:
    isNone = True  # 异常，列表中无内容
while True:
    cho = input('请选择:1.读取存档\t2.新建存档')
    if cho == '1':
        if isNone:
            print('无存档！')
        else:
            name = input('请输入游戏角色名:')
            for i in uLi:
                if i['Name'] == name:
                    print('读取存档成功！')
                    login(i, uLi)
                else:
                    print('读取失败！')
    elif cho == '2':
        name = input('取一个响亮的名字吧:')
        isRegi = False
        for i in uLi:
            print(i)
            if i['Name'] == name:
                print('存档已存在！')
                isRegi = True  # 用户名是否被使用的标识符
                break
        if not isRegi:  # 只有此标识符为False才可以注册
            uDic = {'Name': name, 'Lev': 0, 'Exp': 0, 'HP': 100}
            uLi.append(uDic)
            print('新建存档成功！')
            login(uDic, uLi)
