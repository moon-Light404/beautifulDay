age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
print('今年我的年龄是%d岁'% age)

print('我的名字是%s'% name)

print('我的体重是%5.3f公斤' % weight)
#默认保留到6位小数

print('我的名字是 %s, 今年 %d 岁了' % (name,age+1))


#%s的拓展,所有格式都可以用%s形式输出
print('我的名字是%s，今年%s岁了，体重%s公斤' %(name,age,weight))

#语法f'{表达式}'非常高效
print(f'我的名字是{name},今年{age}岁了')

#print('输出的内容，end='\n') 默认自带换行结束符