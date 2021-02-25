strA = "I don\'t know"
print(strA[::-1])
a = (100,200)
b,c= a
print(b)
print(c)

la = 'python'
print(tuple(la))
print(list(la)) #类型转换
print(ord('中')) #ASCALL码
print(ord('a'))

list1 = ['a','b','c','d','e']
for i in enumerate(list1, start=1):
    print(i)
