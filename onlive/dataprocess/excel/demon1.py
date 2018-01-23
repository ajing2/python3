#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 21:09
# @Author  : lingxiangxiang
# @File    : demon1.py
'''改文件用来打开aaa.xlsx中的内容，并输出到屏幕上'''
import xlrd

def getText():
    data = xlrd.open_workbook("aaa.xlsx")
    table1 = data.sheets()[0]
    for line in range(table1.nrows):
        print(table1.row_values(line))

if __name__ == '__main__':
    getText()