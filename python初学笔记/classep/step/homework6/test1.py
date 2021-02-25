# user = {'小明':[{'id':'1001','name':'烈火战神','type':'火系'}, {'id':'1002','name':'武斗酷猫','type':'草系'}]}
# print(user)
#
# name = input('Please input a name:')
# if name in user.keys():
#     m = input('Please input a id:')
#     for i in user[name]: # i是宠物信息字典
#         if m in i.values():
#             print('aaaaa')
#             break
#     else:
#         print('wrong')

class Person(object):

    def __init__(self, name, Pets):
        self.name = name
        self.Pets = []

    def Keep(self, other):
        self.Pets.append(other)
    def check(self):
        return self.Pets

p = Person('小明',Pets = 'pet')
p.Keep('dog')
p.Keep('cat')
for i in p.Pets:
    print(p.Pets.name)
a = p.check()
print(a)
