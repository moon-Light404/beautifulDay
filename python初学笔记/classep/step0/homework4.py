#随机字符串:
# import random
# def generatestr(randlen = 100):
#     random_str = ""
#     base_str = 'abcdefghigklmnopqrstuvwxyz'
#     length = len(base_str) - 1
#     for i in range(randlen):
#         random_str += base_str[random.randint(0,length)]
#     return random_str
# strA = generatestr()
# print(strA)
# testlist = []
# result = []
#
# dictnum = {}
# for i in strA:
#     if i not in testlist:
#         testlist.append(i)
#         dictnum[i] = strA.count(i)
#
# result = sorted(dictnum.keys())#不可变类型
# print(dictnum)
# for i in range(len(result)):
#     print(f'{result[i]}出现了{dictnum[result[i]]}次')
#
# for key,value in dictnum.items():
#     if value == max(dictnum.values()):
#         print(f'出现最多的字母是{key},出现了{value}')

#
# 输出星期几方法一:
# from datetime import datetime
# def today():
#     today = datetime.now().weekday() + 1
#     if today == 7:
#         today = '天'
#     print(f'今天是星期{today}')
# today()
# # #方法二:
import time
def showDate(a):
    return {
        0 : "星期一",
        1 : "星期二",
        2 : "星期三",
        3 : "星期四",
        4 : "星期五",
        5 : "星期六",
        6 : "星期天"
    }.get(a[6],"时间格式错误")
print("今天是%s" %showDate(time.localtime()))



