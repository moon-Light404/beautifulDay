'''
str() ---将数据转成字符串

tuple() ----将一个序列转换为元组

list() ----将一个序列转换成列表
'''
list1 = [10,20,30]
print(tuple(list1))

t1 = (100,200,300)
print(list(t1))

#  eval() --- 计算在字符串中有效PYthon表达式，返回一个对象


str2 = '1'
str3 ='1.1'
str4 = '(100,200,300)'
str5 = '[100,200,300]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

