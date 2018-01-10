#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 16:54
# @Author  : lingxiangxiang
# @File    : Factorial.py


def one(n):
    total = 1
    if n == 0:
        total = 1
    else:
        for i in range(1, n+1):
            total *= i
    return total

status = 1
while status:
    result = 0
    n = input("please input a number(n>=0): ")
    for i in n:
        # print(i)
        if not i.isdigit():
            print("the number of you input is not int num.")
            exit(1)
    if int(n) < 0:
        print("the number of you input is error.")
        break
    for i in range(0, int(n)+1):
        result += one(i)
    print("0! + 1! + 2! + ... + n! = {0}".format(result))
