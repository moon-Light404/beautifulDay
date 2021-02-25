name_list = ['TOM','Lily','ROSE']
'''
name_list.append('xiaoming')
name_list.append([11,22])
print(name_list)
#1、列表数据可变型
#2、append函数是追加数据的时候如果数据是一个序列，追加整给序列到列表结尾
'''
name_list.extend(['xiaoming','xiaohh'])
print(name_list)
list1 = ['name','age','gender']
list2 = ['Tom',20,'man']
dict1 = {list1[i] : list2[i] for i in range(len(list1))}
print(dict1)