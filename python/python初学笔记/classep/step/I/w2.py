f = open('ff.txt','w+')
#如果有直接覆盖内容，清除内容
#w模式打开文件也就是删除原文件再创建新文件
print(f.read())
f.write('html+css')
#写完之后光标在文件结尾
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read())
f.close()


#Serialzation序列化，将内存中的对象存储下拉，变成字节文件
#dsSerialzation 反序列化，将文件中的字节获取到内存中

