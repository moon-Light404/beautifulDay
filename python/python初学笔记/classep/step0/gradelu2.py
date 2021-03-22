# coding:utf-8
students = []

def menu():
    print('--'*15)
    print('*'*10+"学生成绩管理系统"+"*"*10)
    print("1、添加学生信息")
    print("2、删除学生信息")
    print("3、修改学生信息")
    print("4、查询学生信息")
    print("5、显示所有学生信息")

def add_new():
    print("您选择了添加学生信息功能")
    name = input("请输入学生姓名")
    stuId = input("请输入学生学号")
    grade = input("请输入学生成绩")

    leap = 0
    for temp in students:
        if temp['id'] == stuId:
            leap = 1
            break
        if leap == 1:
            print("输入学生学号重复,添加失败!")
            break
    else:
        stuIn = {}
        stuIn['name'] = name
        stuIn['stuId'] = stuId
        stuIn['grade'] = grade

        students.append(stuIn)
        print("添加成功!")

def change_stu():
    print("您选择了修改学生信息功能")
    stuId = input("输入你要修改的学生学号")

    leap = 0
    i = 0
    for temp in students:
        if temp['id'] == stuId:
            leap = 1
            break
        else:
            i += 1
    if leap == 0:
            print("没有找到该学生的信息,重新输入")
    else:
        grade_m = input("输入要修改后的成绩")
        student[i].grade = grade_m

def del_out():
    print("您选择了删除学生信息")
    stuId = input("请输入要删除学生的学号:")

    leap = 0
    i = 0
    for temp in students:
        if temp['id'] == stuId:
            leap == 1
            break
        else:
            i += 1
    if leap == 0:
        print("没有找到该学生的信息,重新输入")
    else:
        del student[i]
        print("删除学生信息成功!")

def find_info():
    print("您选择了查找学生信息!")
    stuId = input("请输入学生学号:")

    leap = 0
    i = 0
    for temp in students:
        if temp['id'] == stuId:
            leap == 1
            break
        else:
            i += 1
    if leap == 0:
        print("没有找到学生信息，重新输入")
    else:
        print(f'{student[i].name}的成绩是{student[i].grade}')

def printOut():
    print("您选择了显示所有学生信息:")
    print("学号\t\t姓名\t\t成绩")
    for temp in students:
        print("%s\t\t,%s\t\t,%s\t\t" %(temp['id'], temp['name'],temp['grade']))


def main():
    user = '1908328781'
    password = '6807234adc'
    while(True):
        a,b = input('Please input your username and key:').split()
        if (a == user and b == password):
            menu()
            num = int(input("请输入你要选择的选项:"))
            if num == 1:
                add_new()
            elif num == 2:
                del_out()
            elif num == 3:
                change_stu()
            elif num == 4:
                find_info()
            elif num == 5:
                printOut()
        else:
            print("登录失败!")
main()



