import pickle
# f = open('test2.txt','wb+')
# dic = {'name':'ding' ,'go':'aaa', 'aaaa':'bv'}
# dic['name'] = 'jun'
# b1 = pickle.dump(dic,f)
# print(b1)
# dic2 = pickle.loads(b1)
# print(dic2)
# f.close()

import pickle
#通过写二进制的方式打开一个文件
f = open('ser.txt', 'wb')
dic = {'1':'a','2':'b'}
# li = [1,2,3,4,5,6]
#dump(obj,fileObj)
#也可以同时把多个对象序列化进一个文件里，但是反序列化的时候要按照顺序去取
pickle.dump(dic,f)
# pickle.dump(li,f)
f.close()

#coding:utf-8
import pickle
#反序列化
#首先打开之前序列化了的文件，以读二进制的形式 rb
f = open('ser.txt', 'rb')
# for i in range(2):
obj = pickle.load(f)
print(obj)
f.close()


# import pickle
# def xulie(dest,file):
#     pickle.dump(dest,f)
#     file.close()
# f = open('test2.txt','wb')
# dic = {'1':'a','2':'b'}
# xulie(dic,f)
