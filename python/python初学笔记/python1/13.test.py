fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print ('当前水果 :',fruits[index])
print('bye')

#len 返回列表长度
'''
for num in range(10,20):
        for i in range(2,num):
            if num % i ==0:
                j=num/i
                print( '%d等于 %d * %d' % (num,i,j))
                break
        else:
            print('%d是一个质数' % num)
'''

i = 2
while (i<100):
    j = 2
    while (j*j < i):
        if not(i%j) : break
        j = j + 1
    if (j > i/j) : print(f'{i}是素数')
    i = i + 1
print ('Good bye!')



