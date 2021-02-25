#3\猜数字游戏:
import random
a = int(random.uniform(1,100))
i = 0
print("你有五次机会")
for i in range(5):
    num = int(input("请输入你猜的数字:"))
    if num > a:
        print("大了,你还剩余%d次机会" %(4-i))
    elif num == a:
        print("猜对了")
        exit()
    elif num < a:
        if i != 4:
            print("小了,你还剩余%d次机会" %(4-i))
        else:
            print("游戏结束!")
    i += 1
print(f'你要猜的数字是{a},没想到吧')


#猜拳游戏 random左闭右开
# 布 1 石头 0 剪刀 -1
# import random
# temp = 'yes'
# while(temp == 'yes'):
#     type_ = int(input("请选择你的出拳类型(1 代表布, 0 代表石头 -1 代表 剪刀)"))
#     computer = random.randint(-1,1)
#     if (type_ == 1 and computer == 0) or (type_ == 0 and computer == -1) or(type_ == -1 and computer == 1):
#         print("太棒了你赢了!")
#     elif(type_ == computer):
#         print("平局!")
#     else:
#         print("你输了")
#
#
#猜拳游戏:
import random
choDic = {"1":"石头", "2":"剪刀", "3":"布"}
tDic = {"石头":2, "剪刀": 1, "布":0}
temp = 'yes'
while temp == 'yes':
    plCho = choDic.get(input("请输入你的选择:1.石头\t 2.剪刀\t 3.布"),'error')

    if plCho == 'error':
        print('输入错误')
        continue
    comCho = choDic[str(random.randint(1,3))]
    print('你出的是:',plCho,',电脑出的是:',comCho)
    re = tDic[plCho] - tDic[comCho]
    if re == 1 or re == -2:
        print("你赢了")
    elif re == 0:
        print("平局")
    else:
        print("你输了")
    temp = input("是否继续玩?(输入yes or no)")
    if temp == 'no':
        exit()







