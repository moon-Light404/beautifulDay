import pickle
# dic = {'1':'a','2':'b'}
# f = open('ser.txt','wb')
# pickle.dump(dic,f)
# f.close()
#
# f = open('ser.txt','rb')
#
# obj = pickle.load(f)
# print(obj)
# f.close()
# print(obj)

books = ['C语言', 'java程序设计', '小鱼Chash','爱上幼儿园']    #所有的书
f = open('book.txt', 'wb')
pickle.dump(books,f)
f.close()

def checkBook():
    f1 = open('book.txt', 'rb')
    objs = pickle.load(f)
    f1.close()
    print('该借阅系统有以下书籍:')
    print('*'*30)
    print(objs)
    print(f'共有{len(objs)}本书')
checkBook()