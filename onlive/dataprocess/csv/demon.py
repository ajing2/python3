#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 20:51
# @Author  : lingxiangxiang
# @File    : demon.py
import codecs


fileName = "weather.csv"
lineText = list()
with codecs.open(fileName, encoding="utf-8") as f:
    for line in f.readlines():
        print(line.split(","))
        lineText.append(line.split(","))
print(lineText)

print("###"*100)

import csv
with codecs.open(fileName, encoding="utf-8") as fcsv:
    lineCsv = csv.reader(fcsv)
    print(lineText)
    for i in lineCsv:
        print(i)

