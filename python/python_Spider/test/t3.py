# -*- coding: utf-8 -*-
# @Project: testUrlib.py
# @Author: dingjun
# @File name: t3
# @Create time: 2021/3/27 21:04
import xlwt
# 测试excel模块操作
# 导入模块
import xlwt

# 新建工作簿
work_book = xlwt.Workbook()

# 增加sheet表
work_sheet = work_book.add_sheet('Test')

# 单元格操作
work_sheet.write(0,0,'Hello Word')

# 将列表数据写入一个单元格
test_list = [str(i) for i in range(5)]
work_sheet.write_rich_text(1,0,test_list)

# 合并单元格
work_sheet.merge(2,3,0,3)

# 合并单元格并写入
work_sheet.write_merge(4,4,0,3,'合并单元格数据')

# 插入位图
work_sheet.insert_bitmap('01.bmp',5,0)
work_sheet.insert_bitmap('01.bmp',5,8,x=50,y=50,scale_x=1,scale_y=1)

# 保存文件
work_book.save('Test.xls')
