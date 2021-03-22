'''


age = int(input('请输入你的年龄：'))

if age<18:
    print(f'你输入的年龄是{age},童工')
elif (age>=18) and (age<=60):
    print(f'你的年龄是{age},合法')
else:
    print(f'你的年龄是{age},退休年龄')
'''


money = 1
seat = 1

if money == 1:
    print('土豪，请上车')
    #判断是否坐下
    if seat == 1:
        print('有空座，坐下了')
    else:
        print('有空座，站着等...')
else:
    print('朋友，没带钱，跟着跑')
