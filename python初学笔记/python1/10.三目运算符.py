'''
语法
条件成立时 if条件表达式成立 else条件不成立执行另一个表达式
'''

aa = 10
bb = 20
cc = aa - bb if aa>bb else bb- aa #aa<bb执行bb-aa
print(cc)