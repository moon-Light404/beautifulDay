#coding-utf-8
# def user_info(**kwargs):
#     print(kwargs)
# user_info(name = 'Tom',age = 18,id = 110)默认参数放到左边
# #返回一个字典
#


# def test1(name,age = 18,**dic):
#     print(name)
#     print(age)
#     print(dic)
# test1('tyy',20,sex = 'M',height = '181cm',aaa = 12)



'''
def test2(a,b = 10,*tup):
    c = 0
    for i in tup:
        c = c + i
    return c - a - b
print(test2(1,2,10,11,12,13))  b的值被修改了
'''

'''
def test2(a,*tup,b=10):
    print(b)
    c = 0
    for i in tup:
        c += i
    return c - a - b
print(test2(1,2,3,4,5))  #2,3,4,5进入形成元组,b还是默认值
'''

#位置参数，元组参数，默认参数，字典参数
# def test3(name , age,*tup,sex = 'M',**dic):
#     print(name)
#     print(age)
#     print(tup)
#     print(dic)
# test3('tyy',20,'123','abcd','aaa',height = '181cm', work = 'java')





def func4(a,b,*tup,sex = '男',**dic):
    print(a,b)
    print(sex)
    print(tup)
    print(dic)
func4(100,200,1,2,3,4,sex='女',height = '181cm',hobby = '篮球')









