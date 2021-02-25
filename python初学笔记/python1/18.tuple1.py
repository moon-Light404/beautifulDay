
'''
print(dict1['name'])
print(dict1.get('name'))
print(dict1.get('id',110))
print(dict1.get('id'))
'''
dict1 = {'name':'Tom' , 'age' : 20 , 'gender':'男'}
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)
for key, value in dict1.items():
     print(f'{key} = {value}')
     print(key)
     print(value)