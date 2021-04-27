# -*- coding: utf-8 -*-
# @Project: testUrlib.py
# @Author: dingjun
# @File name: testsqlite
# @Create time: 2021/3/27 21:20
import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()   #获取游标

sql =""

c.execute(sql)
conn.commit()
conn.close()
print("opened database successfully")
