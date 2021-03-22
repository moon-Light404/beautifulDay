#通过二进制操作读写文件
f = open('E://腾讯QQ//QQ//鸣人.jpg','rb')

s = f.read()

f1 = open('D://鸣人影分身.jpg','wb')
f1.write(s)
f.close()
f1.close()
