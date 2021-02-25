import pickle
import os
usernames = {}#存放账户密码
userBook = { '190832v':['C语言'], }      #存放用户借的书
f = open('userbook.txt', 'ab')
pickle.dump(userBook,f)
f.close()


books = []    #所有的书
f = open('book.txt', 'ab')
pickle.dump(books,f)
f.close()

obj = {}#反系列化取出来的
mangeuser = 'admin'
mangekey = 'admin'
def Se(dest,file):
    pickle.dump(dest,file)
    file.close()
def Size(filename):
    size = os.path.getsize(filename)
    return size
def menu():
    print('-'*30)
    print('1、注册账号密码')
    print('2、登录账户(请先创建账户)')
    print('3、管理员登录')
    print('4、退出程序')

def register():
    user = input('请输入要注册的账号:')
    password = input('请输入你想要的密码:')
    if Size('user.txt') != 0:
        f = open('user.txt', 'rb')
        obj = pickle.load(f)
        f.close()
        f1 = open('userbook.txt', 'rb')
        user_Book = pickle.load(f1)
        f1.close()
        if user not in obj.keys():
            obj[user] = password
            user_Book [user] = []
            f2 = open('userbook.txt', 'wb')
            pickle.dump(user_Book,f2)
            f2.close()

            f1 = open('user.txt', 'wb')
            pickle.dump(obj, f1)
            f1.close()       #注册的账号不在已经注册的文件里
        else:
            print('该账号已存在!,请重新输入')
    else:
        f1 = open('user.txt', 'wb')
        usernames[user] = password
        pickle.dump(usernames, f1)
        f1.close()

        userBook [user] = []
        f2 = open('userbook.txt', 'wb')
        pickle.dump(userBook, f2)
        f2.close()



def userload():
    try:
        if Size('user.txt') == 0:
            raise Exception('你还未注册账号!')
        f = open('user.txt', 'rb')
        obj1 = pickle.load(f)
        f.close()

    except Exception as a:
        print(a)
        register()
        f = open('user.txt', 'rb')
        obj1 = pickle.load(f)
        f.close()
    try:
        user = input('请输入你的账号:')
        if user not in obj1.keys():
            raise Exception('账号不存在!')
    except Exception as e:
        print(e)

    for key,value in obj1.items():
        if user == key:
            password = input('亲输入你的密码:')
            if password == value:
                print('登录成功')
                choice = int(input('输入你的选项:'))
                if choice == 1:
                    rentBook(user)
                elif choice == 2:
                    checkBook()
                elif choice == 3:
                    deletebook(user)
                elif choice == 4:
                    checkYourBook(user)
            else:
                print('密码错误!')

def deletebook(userName):
    bookname = input('请输入你要还的书(不带引号)')
    f = open('userbook.txt', 'rb')
    totalBook = pickle.load(f)
    f.close()
    print('你当前借的书有:')
    for i in range(len(totalBook[userName]) - 1):
        if totalBook[userName][i] == bookname:
            totalBook[userName].remove(totalBook[userName][i])
            print(totalBook[userName])
            f1 = open('userbook.txt', 'wb')
            Se(totalBook,f1)


    print('删除成功!')

def rentBook(userName):
    newBook = input('请输入你想借阅的书:')
    f = open('userbook.txt', 'rb')
    user_Book = pickle.load(f)
    f.close()

    # f1 = open('book.txt','rb')
    # books = pickle.load(f1)
    # f1.close()

    # if Size('user.txt') == 0:
    #     f = open('userbook.txt', 'wb')
    #     userBook[userName].append(newBook)
    #     Se(userBook,f)
    # else:
    #     f1 = open('userbook.txt','rb')
    #     userBook = pickle.load(f1)
    #     f1.close()
    if (newBook not in user_Book[userName]) :
        f1 = open('userbook.txt', 'wb')
        user_Book[userName].append(newBook)
        Se(user_Book,f1)
    else:
        print('你已经借阅过这本书!')

def checkBook():
    f1 = open('book.txt', 'rb')
    objs = pickle.load(f1)
    f1.close()
    print('该借阅系统有以下书籍:')
    print('*'*30)
    print(objs)
    print(f'共有{len(objs)}本书')


#展示所借的书:
def checkYourBook(user):
    f = open('userbook.txt', 'rb')
    Yourbook = pickle.load(f)
    f.close()
    print('你借的书为:')
    print(Yourbook[user])



def addBooks():
    newBook = input('请输入你要添加的书的名称')
    f2 = open('book.txt', 'rb')
    obj2 = pickle.load(f2)
    f2.close()
    if newBook not in obj2:
        f2 = open('book.txt', 'wb')
        obj2.append(newBook)
        pickle.dump(obj2, f2)
        f2.close()
    else:
        print('该书已经存在,请添加一本新的书:')

def mangerload():
    print('-'*30)
    a = input('请输入你的管理员账号:')
    if a == mangeuser:
        b = input('请输入你的管理员密码:')
        if b == mangekey:
            n = int(input('输入选项 1、添加书籍，2、查看书籍'))
            if n == 1:
                addBooks()
            elif n == 2:
                checkBook()
        else:
            print('你的密码错误!')
    else:
        print('你的账号错误!重新输入')


def main():
    menu()
    while(True):
        n = int(input('请输入你的选项:'))
        if n == 1:
            register()
        elif n == 2:
            userload()
        elif n == 3:
            mangerload()
        elif n == 4:
            exit()
        else:
            print('请输入正确的指令!')
main()

