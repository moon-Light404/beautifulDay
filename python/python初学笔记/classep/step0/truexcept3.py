# sa = 'hello'
# try:
#     int(sa)
# except IndexError as e:
#     print('1',e)
# except KeyError as e:
#     print('2',e)
# except ValueError as e:
#     print('3',e)
# else:
#     print('sucess!')
# finally:
#     print('finally')

# def mul(a,b):
#     if b == 0:#raise指定抛出 的异常
#         raise Exception("除数不能为0")
#     else:
#         return a/b
try:
    a,b = map(int,input("Pease input two number:").split())
    if b == 0:  # raise指定抛出 的异常
        raise Exception("除数不能为0")
except Exception as e:
    print(e)
else:
    print('没有错误')
    print("结果是",a/b)
finally:
    print("我是finally")

