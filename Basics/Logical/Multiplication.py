#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 19:17
# @Author  : lingxiangxiang
# @File    : Multiplication.py

# 1x1=1
# 1x2=2 2x2=4
# 1x3=3 2x3=6 3x3=9

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}x{1}={2} ".format(j, i, i*j), end="")
        if i == j:
            print("")