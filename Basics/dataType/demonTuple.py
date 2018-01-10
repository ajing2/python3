#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 14:55
# @Author  : lingxiangxiang
# @File    : demonTuple.py


l = list()
print(l)
t = tuple()
print(t)

a1 = (1)
a2 = (1,)
# tuple   单元素是，一定要写，否则取法识别是tuple类型
print(type(a1))
print(type(a2))

m = (1, 2, 3, 4, 5, 1, 2, 3, 1, 2)
# count(value)    统计value的个数
print(m.count(1))
# index(value)      返回第一个value元素的下标
print(m.index(5))
print(m.index(2))
