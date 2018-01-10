#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 16:47
# @Author  : lingxiangxiang
# @File    : demonxlutils.py

import xlrd
import xlutils.copy
#打开一个workbook
rb = xlrd.open_workbook('aaa111.xls')
wb = xlutils.copy.copy(rb)
#获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
ws = wb.get_sheet(0)
#写入数据
ws.write(10, 10, 'changed!')
#添加sheet页
wb.add_sheet('sheetnnn2',cell_overwrite_ok=True)
#利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
wb.save('aaa111.xls')
