#使用字典实现switch
def swith_case(n):
    switcher = {
        1 : "周日",
        2 : "周二",
        3 : "周三",
        4 : "周四",
        5 : "周五",
        6 : "周六",
        7 : "周日",
    }
    return switcher.get(n,"nothing")

print(swith_case(4))


