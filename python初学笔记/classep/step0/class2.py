# m = 1
# while m < 10:
#     m = m + 1
#     if m == 5:
#         continue
#     else:
#         print(m)
# print('\n')
# n = 1
# while n < 10:
#     n = n + 1
#     if n == 5:
#         break
#     else:
#         print(n)

#数字反转:
# n = int(input("Please input a number:"))
# temp = 0
# while(n != 0):
#     temp = temp*10 + n%10
#     n //= 10
# print(temp)
#
# n = int(input("Please input a number:"))
# temp = 0
# while(n != 0):
#     temp = n % 10
#     n //= 10
#     print(temp,end="")
#


# #字符串逆置
# str = input("输入:")
# str2 = str[::-1]
# print(str2)

import random

sum = 0
for i in range(6):
    a = float(random.uniform(1,7))
    sum += a
print(sum)
if sum > 20:
    print("大")
else:
    print("小")


