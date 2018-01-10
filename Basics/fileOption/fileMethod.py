#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 19:46
# @Author  : lingxiangxiang
# @File    : fileMethod.py
import codecs

ENCODING = "utf-8"
f = open("1.log",encoding=ENCODING)
# print(dir(f))
print(f.name)
print(f.mode)
print(f.closed)
f.close()

with codecs.open("1.log", "r", encoding=ENCODING) as f:
    print(f.read())