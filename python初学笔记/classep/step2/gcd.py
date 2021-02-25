# 求两数的最大公约数
# def gcd(a,b):
#     m = a
#     n = b
#     if a > b:
#         a,b = b,a
#     while(b != 0):
#         temp = a % b
#         a = b
#         b = temp
#     max = int(m * n / a)
#     print(f'{m}和{n}的最大公因数是{a},最小公倍数是{max}')
# a,b = map(int,input().split())
# gcd(a,b)
#
#
# 删除列表中重复的数据
# def newList_( mylist ):
#     "修改传入的列表"
#     newlist = []
#     for i in mylist:
#         if i not in newlist:
#             newlist.append(i)
#     print(newlist)
#
#
# mylist = [1,1,2,3,3,4,6,7,2,3,4,5,6,7]
# newList_( mylist )
# otherlist = eval(input("请输入你的列表:"))
# newList_( otherlist )

# otherlist = eval(input("请输入你的列表:"))
# newlist = list(set(otherlist))
# print(newlist)
# print(otherlist)

#最大公约数1
# def yue(a,b):
#     re = 0
#     c = a if a < b else b
#
#     while c > 0:
#         if (a % c == 0 and b % c == 0):
#             return c
#         c -= 1
# print(yue(169,13))

#最大公因数2
def yue1(a,b):
    return yue1(b, a % b) if b else a
print(yue1(15,20))
#最小公倍数
# def bei(a,b):
#     c = a if a < b else b
#     while c <= a*b:
#         if (c % a == 0 and c % b == 0):
#             return c
#             break
#         c += 1
# print(bei(15,8))
#
#








