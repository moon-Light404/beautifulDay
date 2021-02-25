#python 常见写模式
# x :写模式，新建一个文件，如果文件存在会报错
# b : 二进制模式，所有数据都可以通过二进制读写
# + : 打开一个文件进行更新，可读可写
# r : 以只读方式打开，文件指针(读取时候)会放到文件开头
#
# + ：可读可写
# b ：二进制读写

f = open('fa.txt','r+')
print(f.readline())
f.seek(0)
print(f.read())
#seek(a,b) a是移动的长度(可正可负) b = 0,1,2
#0是文件开头，1是文件当前，2是文件末尾


f.truncate(3) #从3开始清空
f.seek(0)
print(f.read())
f.close()
