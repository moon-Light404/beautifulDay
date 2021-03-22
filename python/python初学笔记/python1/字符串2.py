'''

name_list = ['TOM','Lily','ROSE']
print(name_list.index('TOM'))
print(len(name_list))
'''

name_list=['TOM','Lily','ROSE']
name = input("输入你的名字:")
if name in name_list:
    print('用户名已存在')
else:
    print('可以注册')