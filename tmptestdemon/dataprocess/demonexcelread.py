#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 14:01
# @Author  : lingxiangxiang
# @File    : demonexcelread.py
import xlrd

def readExcel():
    data = xlrd.open_workbook('test.xlsx')
    table = data.sheets()[0] # 打开第一张表
    nrows = table.nrows # 获取表的行数
    for i in range(nrows): # 循环逐行打印
        print(table.row_values(i))#通过row_values来获取每行的值

readExcel()

# 打开一个workbook
workbook = xlrd.open_workbook('testdata.xlsx')
# 抓取所有sheet页的名称
worksheets = workbook.sheet_names()
print(workbook.sheets())
print('worksheets is {0}'.format(worksheets))
# 定位到sheet1
# worksheet1 = workbook.sheet_by_name(u'Sheet1')
worksheet1 = workbook.sheets()[1]
"""
#通过索引顺序获取
worksheet1 = workbook.sheets()[0]
"""
"""
#遍历所有sheet对象
for worksheet_name in worksheets:
worksheet = workbook.sheet_by_name(worksheet_name)
"""
# 遍历sheet1中所有行row
num_rows = worksheet1.nrows
for curr_row in range(num_rows):
    row = worksheet1.row_values(curr_row)
    print('row%s is %s' % (curr_row, row))
# 遍历sheet1中所有列col
num_cols = worksheet1.ncols
for curr_col in range(num_cols):
    col = worksheet1.col_values(curr_col)
    print('col%s is %s' % (curr_col, col))
# 遍历sheet1中所有单元格cell
for rown in range(num_rows):
    for coln in range(num_cols):
        cell = worksheet1.cell_value(rown, coln)
        print(cell)
