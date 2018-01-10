#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 16:58
# @Author  : lingxiangxiang
# @File    : yinzi.py


for i in range(1, 1000+1):
    l = list()
    for j in range(1, int(i/2)+1):
        if i%j == 0:
            l.append(j)
    sum = 0
    for x in l:
        sum += x
    if sum == i:
        print("{0} 是完数, 因子为：".format(i), end="")
        for x in l:
            print("{0}, ".format(x), end="")
        print("")