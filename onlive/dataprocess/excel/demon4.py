#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 20:38
# @Author  : lingxiangxiang
# @File    : demon4.py

import xlrd
import xlutils.copy

excelr = xlrd.open_workbook("hello.xls")
excelw = xlutils.copy.copy(excelr)
sheet1 = excelw.get_sheet(0)
print(sheet1)
sheet1.write(10, 10, "xlutils.copy")
# sheet1.add_sheet("name")
excelw.save("hello11.xls")