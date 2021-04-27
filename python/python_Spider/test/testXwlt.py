# -*- coding: utf-8 -*-
# @Project: testUrlib.py
# @Author: dingjun
# @File name: testXwlt
# @Create time: 2021/3/27 20:20

import xlwt
# 测试excel模块操作
workbook =  xlwt.Workbook(encoding='utf-8') # 创建Workbook对象
worksheet = workbook.add_sheet('sheet1') # 创建工作表
for i in range(1,10):
    for j in range(1,i+1):
        worksheet.write(i-1,j-1,'%d * %d = %d'%(i,j,i*j)) # 写入数据
workbook.save('九九乘法表.xls') # 保存数据到文件

