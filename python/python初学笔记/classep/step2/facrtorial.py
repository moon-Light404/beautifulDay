#斐波那契数列递归实现
# 1 1 2 3 5
def feibonaqi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return feibonaqi(n-1) + feibonaqi(n-2)
result = feibonaqi(30)
print(result)