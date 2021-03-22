f = open('ff.txt','w')
#只能写,每次写都会覆盖原有的内容,不然要用 'a'
f.write('a')
f.write('python\njava')
f.close()

