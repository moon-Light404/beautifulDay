'''
a = 'hello ' \
    'world'
print(a)
b = 'I\'m TOM'
print(b)
e = how are you
I am OK!
do you do?'''

#print(e) #完整输出

str1 = '012345678'
print(str1[2:8:2])
print(str1[-4:-1])
print(str1[-4:-1:-1])
print(str1[8:5:-1])

print(str1[-1:-4:-1])
print(str1[::-1])#倒序输出
mylist = ['aa','bb','cc']
# aa...bb...cc
new_str = '...'.join(mylist)
print(new_str)