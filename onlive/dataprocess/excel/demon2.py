#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 21:16
# @Author  : lingxiangxiang
# @File    : demon8.py
'''比demon1例子稍微复杂，可以去行数据，列数据，
还可以通过不同的来去的表格
'''
import codecs

import xlrd

data = xlrd.open_workbook("aaa.xlsx")
table2 = data.sheet_by_name("2")
for col in range(table2.ncols):
    print(table2.col_values(col))