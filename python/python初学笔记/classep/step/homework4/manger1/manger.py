import pickle
book = {} #存放书籍信息 {书籍：数量}
userInfo = {}#用户借书的信息  每个用户对应一个列表
uDic = {} #账号密码
f = open('user.txt','ab+') #userInfo
f1 = open('book.txt','ab+') #book
f2 = open('userP.txt','ab+')#存放密码 #userP
#ab+文件指针文件末尾
f.seek(0)
f1.seek(0)
f2.seek(0)
try:
    userInfo = pickle.load(f)
    book = pickle.load(f1)
    uDic = pickle.load(f2)
    f.close()
    f1.close()
    f2.close()
except: #文件为空只能有第一次才会执行
    userInfo = {'190832v':['C语言','PYTHON'],}
    book = {'C语言':3,'PYTHON':3,'概率论':4,}
    uDic = {'190832v':'147258',}
    pickle.dump(userInfo,f)
    pickle.dump(uDic,f2)
    pickle.dump(book,f1)
    f.close()
    f1.close()
    f2.close()



def saveUser():#借书保存信息:
    f = open('user.txt','wb')
    pickle.dump(userInfo,f)
    f.close()
def saveBook():#管理员添加书籍和数量时会保存函数
    f = open('book.txt','wb')
    pickle.dump(book,f)
    f.close()


def returnBook(uName):
    print('你当前借的书有:')
    print(userInfo[uName])
    bookna = input('请输入你要还的书:')
    for i in userInfo[uName]:
        if bookna == i:
            userInfo[uName].remove(i)
        else:
            print('你没借过此书!')



def rentBook(uName):
    bookName = input('请输入你要借的书籍:')
    if bookName in book:
        userInfo[uName].append(bookName)
    else:
        print('该书不存在!')

def adLogin():
    print('-'*30)
    print('admin界面')
    while True:
        n = input('1.添加书籍\t 2.查看所有书籍\t3.保存修改')
        if n == '1':
            bookName = input('请输入你要添加的书籍:')
            if bookName not in book:
                num = int(input('亲输入数量:'))
                book[bookName] = num

            elif bookName in book:
                nu = int(input('请输入要新增的数量:'))
                book[bookName] += nu
        elif n == '2':
            print(book)
        elif n == '3':
            saveBook()
            print('更新书籍成功!')
        else:
            break

def norLogin(uName):
    print('-'*30)
    while True:
        print('用户界面')
        n = input('1.借书\t2.还书\t3.查看个人书籍\t4.记得保存信息,不然借书会失败哦!')
        if n == '1':
            rentBook(uName)
        elif n == '2':
            returnBook(uName)
        elif n == '3':
            print('你借的书为:')
            user = userInfo[uName]
            print(user)
            print('-'*40)

        elif n == '4':
            saveUser()
            print('保存信息成功!')
        else:
            break




#主程序:
while True:
    cho = int(input('请输入你的操作选项:1、登录 \t 2、注册'))
    if cho == 1:
        n = int(input('请输入登录选项:1、用户登录. 2、管理员登录'))
        if n == 1:
            uName = input('请输入账号')
            uPsw = input('请输入密码:')
            try:
                if uName not in uDic.keys():
                    raise  Exception('账号不存在')
                elif uDic[uName] != uPsw:
                    raise Exception('密码错误')
                else:
                    print('登录成功')
                    norLogin(uName)
            except Exception as e:
                print(e)
        elif n == 2:
            uName = input('请输入账号')
            uPsw = input('请输入密码:')
            if uName == 'admin' and uPsw == 'admin':
                adLogin()
            else:
                print('账号或密码错误!')


    elif cho == 2:
        uName = input('请输入新的账号:')
        uPsw = input('请输入密码:')
        uDic[uName] = uPsw
        print('注册成功')
        f = open('userP.txt','wb')
        pickle.dump(uDic,f)
        f.close()

    elif cho == 3:
        print('欢迎下次光临--------')
        exit()