#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 14:46
# @Author  : lingxiangxiang
# @File    : papertest.py

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}x{1}={2} ".format(j, i, i*j), end="")
        if i == j:
            print("")