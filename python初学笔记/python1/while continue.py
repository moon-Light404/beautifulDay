i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print('媳妇，我错了')
    i += 1
else:
    print('媳妇原谅我了')
'''
加了continue后循环是正常结束的，else下方的代码会执行
'''
