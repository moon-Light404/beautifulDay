# 2.买鸡问题，你有100块钱，公鸡5块钱一只，母鸡3块钱一只，小鸡一块钱3只，钱花光
#     	分别写出买的方法(公鸡买了20只，母鸡买了0只，小鸡买了0只)
#     	求出共有多少种买法

c = 3
count = 0
for i in range(0,21):
    for j in range(0,34):
        for k in range(0,34):
            if (i * 5 + j * 3 + k * 3 == 100):
                print(f'公鸡买了{i}只,母鸡买了{j}只,小鸡买了{k}只')
                count = count + 1


print(f'总共有{count}种')
