# elif ...
# elif ...
# elif ...
# elif ...
# elif ...  从上往下判断表达式是否为真，为真则执行对应的语句块，
#后续不会在判断

# if ...
# if ...
# if ...
# if ...  每一个都会判断，这样会浪费时间和内存
# a = int(input("输入一个数"))
# if a == 1:
#     print("hello")
# if a == 2:
#     print("hhh")
# if a < 3:
#     print("sawfwag")

# list1 = []
# print("输入四个数")
# for i in range(4):
#     a = int(input())
#     list1.append(a)
# b = list1[0]
# for p in range(1,len(list1)):
#     if list1[p] > b:
#         b = list1[p]
# print(b)

a,b,c,d = map(int,input().split())
print(a)
print(b)
print(c)
print(d)
