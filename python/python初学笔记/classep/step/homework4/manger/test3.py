# import pickle
# books = ['C语言', 'java程序设计', '小鱼Chash','爱上幼儿园']    #所有的书
# f = open('book.txt','wb')
# pickle.dump(books,f)
# f.close()
#
#
# newBook = input('请输入你要添加的书的名称')
# f2 = open('book.txt', 'rb')
# obj2 = pickle.load(f2)
# f2.close()
# if newBook not in obj2:
#     f2 = open('book.txt','wb')
#     obj2.append(newBook)
#     pickle.dump(obj2,f2)
#     f2.close()
# else:
#     print('该书已经存在,请添加一本新的书:')
#
# def checkBook():
#     f1 = open('book.txt','rb')
#     objs = pickle.load(f1)
#     f1.close()
#     print('该借阅系统有以下书籍:')
#     print('*'*30)
#     print(objs)
#     print(f'共有{len(objs)}本书')
# checkBook()



list = ['aa','goc++','Gojava']
n = input('L:')
for i in range(len(list)-1):
    if n == list[i]:
         list.remove(list[i])
\
print(list)