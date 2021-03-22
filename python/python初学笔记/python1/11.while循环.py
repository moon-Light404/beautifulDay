'''


sum=0
i= int(input('输入数字'))
while i>=1:
    if i%2 == 0:
        sum+=i
    i-=1
print(sum)
'''

i = 1
while i<=5:

    if i == 3:
        print('这边说得不好')
        break
    print('媳妇我错了')
    i += 1
else:
    print('媳妇，原谅我，真开心')
# else指的是循环正常结束之后要执行的代码，如果是break终止循环的情况，else
#下方缩进的代码将不执行
