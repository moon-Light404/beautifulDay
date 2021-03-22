# def ThrowErr():
#     raise Exception("抛出一个异常")
# ThrowErr()

# try:
#     raise NameError('Hi')
# except NameError:
#     print('你真的有问题')
#     raise

# class FError(Exception):
#     print('异常')
# try:
#     raise FError('自定义异常')
# except FError as e:
#     print(e)
    # raise




# try:
#     raise Exception('发生异常')
# except Exception as e:
#     print(e)
# finally:
#     print('finally')

try:
    print(2/0)
except ZeroDivisionError:
    print('除数不能为0')
except Exception:
    print('其他类型异常')

try:
    print(2/0)
except(ZeroDivisionError,Exception):
    print('发生了一个异常')


try:
    print(2/0)
except(ZeroDivisionError,Exception) as e:
    print(e)
#ZeroDivisionError 自带division by zero








