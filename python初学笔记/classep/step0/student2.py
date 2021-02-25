students = []


def meun():
    print("=" * 30)
    print("*" * 10 + "学生信息管理" + "*" * 10)
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.指定学号查询学生信息")
    print("4.查询全部学生信息")
    print("5.保存信息")
    print("0.退出系统")
    print("=" * 30)


def add_new_info():
    global students
    print("您选择了添加学生信息功能")
    name = input("请输入学生姓名：")
    stuId = input("请输入学生学号(学号不可重复)：")
    age = input("请输入学生年龄:")
    # 验证学号是否唯一
    i = 0
    leap = 0
    for temp in students:
        if temp['id'] == stuId:
            leap = 1
            break
        else:
            i = i + 1
        if leap == 1:
            print("输入学生学号重复，添加失败！")
            break
    else:
        # 定义一个字典，存放单个学生信息
        stuInfo = {}
        stuInfo['name'] = name
        stuInfo['id'] = stuId
        stuInfo['age'] = age

        # 单个学生信息放入列表
        students.append(stuInfo)
        print("添加成功！")


def del_info():
    global students
    print("您选择了删除学生功能")
    delId = input("请输入要删除的学生学号:")
    # i记录要删除的下标，leap为标志位，如果找到leap=1，否则为0
    i = 0
    leap = 0
    for temp in students:
        if temp['id'] == delId:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 0:
        print("没有此学生学号，删除失败！")
    else:
        del students[i]
        print("删除成功！")


def search_info():
    global students
    searchID = input("请输入你要查询学生的学号:")

    # 验证是否有此学号
    i = 0
    leap = 0
    for temp in students:
        if temp['id'] == searchID:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 0:
        print("没有此学生学号，查询失败！")
    else:
        print("找到此学生，信息如下：")
        print("学号：%s\n姓名：%s\n年龄：%s\n" % (temp['id'], temp['name'], temp['age']))


def print_all_info():
    print("序号\t\t学号\t\t姓名\t\t年龄")
    for temp in students:
        print("sno:%s,stuName:%s,stuAge:%s" % (temp['id'], temp['name'], temp['age']))
        print("*" * 20)


def loda_data():
    # 加在之前存储的数据
    global students
    f = open("info_data.data")
    content = f.read()
    info_list = eval(content)
    f.close()


def main():
    # 加在数据（先存好数据，在打开这个数据直接读取数据）
    # load_data()
    while True:
        # 1.打印工程
        meun()
        # 2.获取用户的选择
        key = input("请输入要进行的操作）：")
        # 3.根据用户的选择，作出相应的事件
        if key == "1":
            add_new_info()
        elif key == "2":
            del_info()
        elif key == "3":
            search_info()
        elif key == "4":
            print_all_info()
        elif key == "5":
            save_data()
        elif key == "0":
            exit_flag = input("你确定要退出吗？(yes or no)")
            if exit_flag == "yes":
                break
            else:
                print("输入有误，请重新输入。。。")
                input("\n\n\n按回车键可以继续。。。")
                continue
            # 程序开始


main()