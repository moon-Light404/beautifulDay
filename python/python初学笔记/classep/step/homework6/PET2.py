class Dog(object):
    Dog_total = ['金毛','哈士奇','泰迪']
    __slots__ = ('name','type','sex')
    def __init__(self,name,type,sex):
        self.name = name
        self.type = type
        self.sex = sex

    def __str__(self):
        return '品种:%s,性别:%s,名字:%s'%(self.type,self.sex,self.name)


class Person(object):

    count = 0
    def __init__(self,name):
        self.name = name
        self.Pets = []
    #领养狗狗
    def Keep(self,other):
        self.Pets.append(other)
        Person.count += 1
        print('你领养了%s' %(other.name))

    #给朋友狗狗
    def Send_dog(self,other_person,_dog):
        for i in self.Pets:
            if i.name == _dog:
                self.Pets.remove(i)
                other_person.Pets.append(i)
    #返回收养的狗狗
    def Check_dog(self):
        return self.Pets
    def print_Dogs(self):
        print(f'你领养了{self.count}只狗狗')
        for i in self.Pets:
            print(i)
#-------------------选项--------------------
def choDogType(cho):
    return{
        '1':'金毛',
        '2':'哈士奇',
        '3':'泰迪',
    }.get(cho,'non')

def choDogSex(cho):
    return{
        '1':'boy',
        '2':'girl',
    }.get(cho,'non')
#-----------------------------------------
def main():
    name = input('请输入你的名字:')
    p1 = Person(name)
    while True:
        n = input('请输入你的选择:1.领养狗狗\t 2.与狗狗玩耍\t 3.喂食\t 4.查看所领养狗狗的信息' + \
                  '5.给朋友狗狗')
        if n == '1':
            for i in enumerate(Dog.Dog_total,start = 1):
                print(i)
            dogTy = choDogType(input('你要领养的狗狗品种:'))
            if dogTy == 'non':
                print('选项不存在!')
            dogName = input('取个名字')
            dogSex = choDogSex(input('输入性别:1.boy 2.girl'))
            if dogSex == 'non':
                print('选项不存在')
            d1 = Dog(dogName,dogTy,dogSex)
            p1.Keep(d1)

        elif n == '2':
            if len(p1.Pets) <= 0:
                print('你还没有狗子')
            else:
                Dname = input('你想玩耍哪只狗狗:')
                Dog_keep = p1.Check_dog()
                for i in Dog_keep:
                    if i.name == Dname:
                        print(i)
                        print('你正在玩耍%s' % i.name)
                        break
                else:
                    print('你没有领养该宠物!')
        elif n == '3':
            Dname = input('你想喂食那只狗狗:')
            Dog_keep = p1.Check_dog()
            for i in Dog_keep:
                if  i.name == Dname:
                    print(i)
                    print('你正在喂食%s' % i.name)
                    break
            else:
                print('你没有领养该宠物!')
        elif n == '4':
            if p1.Pets:
                p1.print_Dogs()
            else:
                print('无狗！')
        elif n == '5':
            other_person = input('请输入朋友的名字')
            p2 = Person(name)
            dog_name = input('请输入狗狗的名字:')
            p1.Send_dog(p2,dog_name)
            print('赠送成功!')
        else:
            break
if __name__ == '__main__':
    main()







