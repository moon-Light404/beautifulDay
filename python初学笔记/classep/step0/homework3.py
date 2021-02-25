# count = 0
# for i in range(1,9):
#     for j in range(1,12):
#         m = 36 - i * 4 - j * 3
#         if m >= 1 and i + j + m*2 == 36:
#             print(f'成年男子{i}人,成年女子{j}人,小孩{m*2}人')
#             count += 1
# print(f'有{count}种')
# # for i in range(9):
# #     print(i)
# sum = 0
# for i in range(0,101,2):
#     sum += i
# print(sum)
#
#
# s = 0
# for i in range(101):
#     if i % 2 == 0:
#         s += i
# print(s)
#


# 九九乘法表:
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}','=',j * i,end = "   ")
#     print('\n')



#2\打印图形
n = int(input("请输入一个数字:"))
for i in range(n,0,-1):
    print((n-i)*'@', end = "")
    print((2*i - 1)*'*')





#查找指定范围内的素数：
# lower = int(input("输入最小值"))
# upper = int(input("输入最大值"))
#
# for num in range(lower,upper + 1):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i == 0):
#                 break
#         else:
#             print(num,end = "  ")




#阶乘运算递归:
# num = int(input())
# factorial = 1
#
# if num < 0:
#     print("输入错误无效")
# elif num == 0:
#     print("0的阶乘为1")
# else:
#     for i in range(1,num+1):
#         factorial = factorial * i
#     print(f'{num}的阶乘是{factorial}')
#


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# def main():
#     num = int(input("Please input a number:"))
#     a = int(factorial(num))
#     print(a)
#
# main()




#while循环
# i = 2
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     i += 2
# print(sum)




#斐波那契数列
