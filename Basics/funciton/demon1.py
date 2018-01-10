#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 10:48
# @Author  : lingxiangxiang
# @File    : demon1.py

def add(args):
    total = 0
    for i in args:
        total += i
    return total


def main():
    number = list()
    s = input("plase input digit like(a + b + c + d + ...): ")
    for num in s.split("+"):
        number.append(int(num.strip()))
    print(add(number))

if __name__ == '__main__':
    main()

