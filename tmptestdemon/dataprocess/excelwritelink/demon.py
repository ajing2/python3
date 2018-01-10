#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 16:05
# @Author  : lingxiangxiang
# @File    : demon.py

import codecs
import xlwt
book = xlwt.Workbook()
sheet_index = book.add_sheet('index')
line=0
for i in range(9):
    link = 'HYPERLINK("{0}.txt", "{1}_11111")'.format(i, i)
    sheet_index.write(line, 0, xlwt.Formula(link))
    line += 1
book.save('simple2.xls')
for i in range(0, 9):
    file = str(i) + ".txt"
    with codecs.open(file, 'w') as f:
        f.write(str(i)*10)
