import random
import pickle
Userinfo = {}

#产生随机数
def randomindex():
    randnum = random.uniform(0,100)
    if 0 < randnum <= 10:
        return 1  #shilaike
    elif 10 < randnum <=30:
        return 2  #wolfman
    elif 30 < randnum <=100:
        return 3   #caixukun

#数据序列化写数据
def Se(d,file):
    pickle.dump(d,file)
    file.close()
数据反序列化读数据
def Dse(f):
    try:
        temp = pickle.load(f)
        f.close()
        return temp
    except:
        print('读取信息出错,重试')




#更新等级:exp指的是打怪的经验
def Rank(exp):
    a = exp // 100
    return a



#怪物信息
def shilaike(exp,HP):
    exp += 30
    hurts = [10,15,20]
    HP -= random.choice(hurts)



def wolfman(exp,HP):
    hurts = [30,45,50]
    exp += 80
    HP -= random.choice(hurts)




def caiXukun(exp,HP):
    hurts = [50,100,150]
    exp += 250
    HP -= random.choice(hurts)

休息时的经验值
def breakdown():
    HP += random.uniform(10,20)



def prinInfo(nam):
    f = open('info.txt','rb')
    userTotal = Dse(f)
    print(f'亲爱的{userTotal[nam]},当前你的HP为{userTotal[nam]['HP']}, 等级为{userTotal[nam]['rank']})




#与存档一起使用 #探险模式#
def brave(user):
    f = open('info.txt','rb')
    Usertotal = pickle.load(f)
    f.close
    a = randomindex()
    f = open('info.txt','wb')
    if a == 1:
        shilaike(Usertotal['user']['exp'],Usertotal['user']['HP'])
        rank = Rank(Usertotal[user]['exp'])
        Usertotal[user]['rank'] = rank
        pickle.dump(Usertotal,f)
        f.close()
    elif a == 2:
        wolfman(Usertotal['user]['exp'],Usertotal['user']['HP'])
        Usertotal[user]['rank'] = Rank(Usertotal[user]['exp'])
        pickle.dump(Usertotal, f)
        f.close()
    elif a == 3:
        caiXukun(Usertotal['user]['exp'],Usertotal['user']['HP'])
        Usertotal[user]['rank'] = Rank(Usertotal[user]['exp'])
        pickle.dump(Usertotal, f)
        f.close()



#注册角色
def register():
    print('现在正在注册页面:')
    try:
        f = open('info.txt','rb')
        userTotal = pickle.load(f) #返回一个双层字典
        f.close()
    except:#如果为空
        print('你是第一个角色')
        name = input('请输入角色的昵称:')
        userT = {}
        userT[name]['HP'] = 0
        userT[name]['exp'] = 0
        userT[name]['rank'] = 0
        f = open('info.txt','wb')
        pickle.dump(userT,f)
        f.close()

    else:
        f = open('info.txt', 'rb')
        userTotal = pickle.load(f)
        f.close()# 返回一个双层字典
        name = input('请输入角色的昵称:')
        if name not in userTotal.keys():
            userTotal[name]['HP'] = 0
            userTotal[name]['exp'] = 0
            userTotal[name]['rank'] = 0
            f = open('info.txt','wb')
            pickle.dump(userTotal,f)
            f.close()
            print('注册成功!')



def menu():
    print('-'*30)
    print('欢饮来到勇者大冒险----')
    print('1、读取存档')
    print('2、新建存档')



#玩家选项
def secmenu():
    print('下一步你想干什么，请选择(记得存档)：')
    print('a、探险')
    print('b、休息')
    print('c、查看角色信息')
    print('d、存档退出')
    while(choice != 'd'):
        choice = input('请输入你下一步操作:__')
        if choice == 'a':
            brave(n)
        elif choice == 'b':
            print('aaa')
        elif choice == 'c':
            print('gg')
        elif choice == 'd':
            exit()




#登录
def load():
    try:
        n = input('请选择存档角色:')
        f = open('info.txt','rb')
        userinfo = pickle.load(f)
        f.close()
    except:
        print('还没有注册!')

    else:
        n = input('请选择存档角色:')
        f = open('info.txt', 'rb')
        userinfo = pickle.load(f)
        f.close()
        if n in userinfo.keys():
            print('登录成功!')
            secmenu()



def main():
    menu()
    while(True):
        n = int(input('输入操作:'))
        if n == 1:
            load()
        elif n == 2:
            register()
        elif n == 2:
            exit()


main()

