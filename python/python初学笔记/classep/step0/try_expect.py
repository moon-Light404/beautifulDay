# import traceback
# try:
#     print(5/0)
# except (TypeError,ZeroDivisionError) as e:
#     traceback.print_exc()
#     print(e) #输出错误信息
# else:
#     print("没错误!")

def mul(a,b):
    if a<b:
        raise BaseException('被减数不能小与简述')
    else:
        return a - b
try:
    print(mul(0,3))
    print('try的结尾')
except:
    pass
    raise
finally:#抛出异常

    print('finally')
