names = []
grades = []
print('欢迎来到成绩录入系统')
print('-------------------------')
print('1、查询', '2、修改', '3、录入', '4、删除' ,'5、显示所有信息')

temp = int(input('请输入你的操作:'))

if temp == 1:
    name_1 = input('请输入要查询的名字:')
    if name_1 in names:
        a = names.index(name_1)
        print(f'{name_1}的成绩是{grades[a]}')
    else:
        print('未找到该学生的信息!')
elif temp == 2:
    name_2 = input('请输入要修改人的名字:')
    b = names.index(name_2)
    grade = int(input('请输入要修改的成绩:'))
    grades[b] = grade
    print('修改成功!')
elif temp == 3:
    print('请输入添加人的名字和成绩:')
    name_3 = input()
    grade = int(input())
    names.append(name_3)
    grades.append(grade)
elif temp == 4:
    name_4 = input('请输入删除人的名字:')
    if name_4 in names:
        names.remove(name_4)
        grades.remove(grades(names.index(name_4)))
        print('修改成功!')
    else:
        print('不存在此人')
else:
    for name in names:
        print(name,end = "")
    for grade in grades:
        print(grade,end = " ")
#驼峰式命名法
# stuName = []
# stuScore = []
# ventilate