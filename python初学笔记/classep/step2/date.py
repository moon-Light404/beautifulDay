# import time
# localtime = time.localtime(time.time())
# print("本地时间为",localtime)
#
#
# print(time.gmtime())
#
# t = (2020,9,11,8,0,0,4,255,0)
# print(time.mktime(t))
# print(time.mktime(time.localtime())) mk转换为时间戳
#
#
# print(time.asctime(time.localtime()))
# #传时间戳作为参数
# print(time.ctime())

#让程序睡眠:
# time.sleep() #参数为秒数

# print("now is :")
# def sleepTime():
#     print(time.ctime())
#     time.sleep(5)
#     print(time.ctime())
# sleepTime()

import time

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式


# 将格式字符串转换为时间戳
