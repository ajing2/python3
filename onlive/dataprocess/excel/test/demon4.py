#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 21:52
# @Author  : lingxiangxiang
# @File    : demon4.py

import codecs
import xlwt
book = xlwt.Workbook()
sheet_index = book.add_sheet('index')

for i in range(9):
    link = 'HYPERLINK("{0}.txt", "{1}_11111")'.format(i, i)
    sheet_index.write(i, 0, xlwt.Formula(link))

book.save('simple2.xls')
for i in range(0, 9):
    file = str(i) + ".txt"
    with codecs.open(file, 'w') as f:
        f.write(str(i)*10)
