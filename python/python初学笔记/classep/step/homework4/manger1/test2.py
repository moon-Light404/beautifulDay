# userInfo = {'19032v':['C语言','PYTHON'],}
# def nn(uName):
#     print(userInfo[uName])
#
# n = input()
# nn(n)


lis = ['C语言','JAVA']
n = input()
for i in lis:
    if n == i:
        lis.remove(i)
print(lis)