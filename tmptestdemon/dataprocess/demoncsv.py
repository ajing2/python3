#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 13:33
# @Author  : lingxiangxiang
# @File    : demoncsv.py

import csv

fileName = 'weather.csv'
with open(fileName, "r", encoding="utf-8") as f:
    text = csv.reader(f)
    for i in text:
        print(i)
print("####"*10)
with open(fileName, "r", encoding="utf-8") as f:
    for i in f.readlines():
        print(i.split(","))