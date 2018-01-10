#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 15:16
# @Author  : lingxiangxiang
# @File    : demonexcelwrite.py
import xlwt
#创建workbook和sheet对象
workbook = xlwt.Workbook() #注意Workbook的开头W要大写
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
sheet2 = workbook.add_sheet('sheet2', cell_overwrite_ok=True)
sheet3 = workbook.add_sheet('sheet3', cell_overwrite_ok=True)
#向sheet页中写入数据
sheet1.write(0,0,'this should overwrite1')
sheet1.write(0,1,'aaaaaaaaaaaa')
sheet2.write(0,0,'this should overwrite2')
sheet2.write(1,2,'bbbbbbbbbbbbb')

#-----------使用样式-----------------------------------
#初始化样式
style = xlwt.XFStyle()
#为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
#设置样式的字体
style.font = font
#使用样式
sheet3.write(0,1,'some bold Times text',style)

#保存该excel文件,有同名文件时直接覆盖
workbook.save('test2.xls')
print('创建excel文件完成!')
