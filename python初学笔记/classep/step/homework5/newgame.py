#coding:utf-8
from datetime import datetime
import random
import pickle
uli = []  #存放玩家信息，玩家信息为字典
uDic = {}
def uplev(uDic):
    n = uDic['exp'] // 100
    if n > uDic['lev']:
        print('升到了%d级' %n)
        num = random.randint(50,100)
        uDic['HP'] = uDic['HP'] + num
        print('HP回复%d' %num)
        print('当前血量HP%d' %uDic['HP'])
    else:
        print('当前血量HP%d' %uDic['HP'])
def sleepH(uDic):
    num = random.randint(10,20)
    uDic['HP'] = uDic['HP'] + num
    print('可以休息,HP回复%d' %num)
    return datetime.now()

def show(uDic):
    print('你的昵称是%s,当前等级%d,经验值%d,HP为%d' %(uDic['Name'],uDic['lev'],uDic['exp'],uDic['HP']))


def attack(a,b,c):
    num = random.randint(1,3)
    if num == 1:
        return a
    elif num == 2:
        return b
    else:
        return c

def fight(uDic):
    monum = random.randint(1,100)

    if monum > 90:
        at = attack(50,100,150)
        print('你遇到了菜虚焜你受到了%d伤害' %at)

        if uDic['HP'] <= at:
            print('你被菜虚鲲击败了！')
            uDic['HP'] = 0
        else:
            print('你击败了菜虚鲲，获得了250经验值，获得了300HP')
            uDic['exp'] += 250
            uDic['HP'] = uDic['HP'] + 300 - at
            uplev(uDic)
    elif monum > 70:
        at = attack(30,45,50)
        print('你遇到了狼人，受到了%d伤害!' %at)

        if uDic['HP'] <= at:
            print('你被狼人击败了')
            uDic['HP'] = 0
        else:
            print('你击败了狼人，获得了80经验值')
            uDic['exp'] += 80
            uDic['HP'] = uDic['HP'] -at
            uplev(uDic)
    else:
        at = attack(10,15,20)
        print('你遇到了史莱克,受到了%d伤害' %at)
        if uDic['HP'] <= at:
            print('你被史莱克击败了')
            uDic['HP'] = 0
        else:
            print('你击败了史莱克，获得了30经验')
            uDic['exp'] += 80
            uDic['HP'] = uDic['HP'] - at
            uplev(uDic)






def login(uDic,uli):
    show(uDic)
    isFir = True
    t1 = datetime.now()
    while True:
        choice = int(input('请输入你的操作:1、探险\t2、休息\t 3、查看信息\t 4、存档退出'))
        if choice == 1:
            fight(uDic)
        elif choice == 2:
            t2 = datetime.now()
            if (t2-t1).total_seconds() > 10 or isFir:

                isFir = False
                t1 = sleepH((uDic))
            else:
                print('每10s休息一次,不要偷懒哦')
        elif choice == 3:
            show(uDic)
        else:
            f = open('info1.txt','wb')
            pickle.dump(uli,f)
            f.close()
            print('存档成功!')
            exit()



print('-----欢迎来到勇者大冒险游戏---')

flag = False
try:
    f = open('info1.txt','rb')
    uli = pickle.load(f)
    print(uli)
    f.close()
except:
    flag = True
def main():
    while True:
        choice = int(input('请选择:1、读取存档\t2、新建存档'))
        if choice == 1:
            if flag == True:
                print('无存档!')
            else:
                name = input('请输入游戏角色名:')
                for i in uli:
                    if i['Name'] == name:
                        print('读取存档成功!')
                        login(i,uli)
                    else:
                        print('读取失败!')
        elif choice == 2:
            name = input('取一个名字:')
            Is = False
            for i in uli:
                if i['Name'] == name:
                    print('存档已存在!')
                    Is = True
                    break
            if not Is:
                uDic = {'Name':name,'lev':0,'exp':0,'HP':100}
                uli.append(uDic)
                print('新建存档成功!')
                login(uDic,uli)
main()