'''

for letter in 'Python':
    if letter == 'h':
        pass
        print('这是pass块')
    print(f'当前字母:{letter}')
    '''
    #pass 一般用来占位置，因为如果定义一个空函数程序会报错，没想好
    #写什么可以用pass填充，使其运行
#九九乘法表

j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j} ={i*j}  ' ,end='')
        i += 1
    print()
    j += 1




