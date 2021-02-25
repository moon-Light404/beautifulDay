# print(hasattr(stu1,'age'))
#
# print(getatrr(stu1,'age'))#得到某个值
#
# setattr(obj,attr,value) #设置某个值
#
# delattr((stu1,'age')) #删除对象某个属性


class Student(object):
    def setAge(self,age):
        if not isinstance(age,int):
            raise ValueError('年龄必须为整数!')
        elif age < 0 or age > 200:
            raise ValueError('年龄必须在0~200之间')
        self.age = age

s = Student()
try:
    s.setAge(-2)
    print('学生年龄为%d' %s.age)
except ValueError as e:
    print(e)