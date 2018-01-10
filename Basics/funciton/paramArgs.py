#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 13:02
# @Author  : lingxiangxiang
# @File    : paramArgs.py
def add(*args):
    total = 0
    for i in args:
        total +=i
    print("total = {0}".format(total))


def sortDictValue(dict1):
    print(sorted(dict1.items(), key=lambda d:d[1], reverse=False))


if __name__ == '__main__':
    add(1, 2, 3, 4, 5)
    s1 =lambda x, y: x+y
    # def s1(x, y):
    #     return x+y
    print(s1(10 ,20))
    aaa = dict(a=100, b=10, c=50, d=321)
    for i in aaa.items():
        print(i[1])
    print(aaa)
    l = list()
    sortDictValue(aaa)



