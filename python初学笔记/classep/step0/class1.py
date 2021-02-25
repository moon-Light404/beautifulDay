# user = 'admin'
# secret = 'psw123'
# a,b = input("请输入账号密码:(空格隔开)").split()
# if a == user and b == secret:
#     print("登录成功!")
# else:
#     print("登录失败!")

grade = int(input("请输入一个成绩分数:"))
if grade >= 90:
    print("成绩为A")
elif grade >= 80:
    print("成绩为B")
elif grade >= 70:
    print("成绩为C")
elif grade >= 60:
    print("成绩为D")
else:
    print("成绩为E")
