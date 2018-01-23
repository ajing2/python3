#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 20:47
# @Author  : lingxiangxiang
# @File    : demon5.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 21:40
# @Author  : lingxiangxiang
# @File    : demon9.py
'''写一个新的excel文件'''

import xlwt

excel = xlwt.Workbook("hello11.xls")
sheet1 = excel.add_sheet("sheet1")
sheet2 = excel.add_sheet("sheet2")
sheet3 = excel.add_sheet("sheet3")

sheet1.write(0,0, "hello world")
sheet1.write(1,0, "hello")
sheet1.write(2,0, "ajing")

#
style = xlwt.XFStyle()
#为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
#设置样式的字体
style.font = font
#使用样式
sheet3.write(0,1,'some bold Times text',style)


excel.save("hello11.xls")
print("创建hello11.xls完成")
