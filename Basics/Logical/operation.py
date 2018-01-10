#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 16:29
# @Author  : lingxiangxiang
# @File    : operation.py
'''
python 解决数学难题
ABCD乘9=DCBA，A=? B=? C=? D=? 答案：a=1,b=0,c=8，d=9      1089*9=9801
'''

for A in range(0, 10):
    for B in range(0, 10):
        for C in range(0, 10):
            for D in range(0, 10):
                start = 1000 * A + 100* B + 10 * C + D
                end =  1000* D + 100 * C + 10 * B + A
                if start * 9 == end:
                    print("A = {0}".format(A))
                    print("B = {0}".format(B))
                    print("C = {0}".format(C))
                    print("D = {0}".format(D))
                    print("{0} * 9 = {1}".format(start, end))

