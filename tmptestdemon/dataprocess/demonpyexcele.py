#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 17:59
# @Author  : lingxiangxiang
# @File    : demonpyexcele.py

import pyExcelerator
#创建workbook和sheet对象
wb = pyExcelerator.Workbook()
ws = wb.add_sheet(u'第一页')
#设置样式
myfont = pyExcelerator.Font()
myfont.name = u'Times New Roman'
myfont.bold = True
mystyle = pyExcelerator.XFStyle()
mystyle.font = myfont
#写入数据，使用样式
ws.write(0, 0, u'hello lingxiangxinag！', mystyle)
#保存该excel文件,有同名文件时直接覆盖
wb.save('mini.xls')
print('创建excel文件完成！')


import pyExcelerator
#parse_xls返回一个列表，每项都是一个sheet页的数据。
#每项是一个二元组(表名,单元格数据)。其中单元格数据为一个字典，键值就是单元格的索引(i,j)。如果某个单元格无数据，那么就不存在这个值
sheets = pyExcelerator.parse_xls('mini.xls')
print(sheets)
