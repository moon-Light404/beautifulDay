dict1 = {'name':'Tom', 'age': 20 , 'gender': ' 男'}
# print(dict1['name'])
# for item in dict1.items():
#     print(item)
# for key,value in dict1.items():
#     print(f'{key} = {value}')

# user = dict()
# zhangHu = input('请输入你的账户')
# secret = input('输入你的密码')
# user[zhangHu] = secret
# print('创建账户成功!')


#增加字典对象
dict1.update({"gender":"女"})
dict1.update({"home":"jiangxi"})
print(dict1)

# book_dict = dict()
# my_temp_dict = {'name':'王外' , "age":18}
# book_dict.update(**my_temp_dict)
# print(book_dict)


#删除key - value
# del dict1['name']
# print(dict1)