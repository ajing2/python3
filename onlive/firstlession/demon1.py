#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 20:45
# @Author  : lingxiangxiang
# @File    : demon1.py


class CountNumber(object):
    '''ABCD * 9 = DCBA
    通过计算机的方法，给我们计算出A = ?  B = ? C = ? D = ?
    A: 1-9
    B: 0-9
    C: 0-9
    D: 1-9
    A != B != C !=D
    '''
    def __init__(self):
        print("ABCD * 9 = DCBA; A!=B!=C!=D")
    def numAbcd(self):
        for A in range(1, 10):
            for B in range(0, 10):
                for C in range(0, 10):
                    for D in range(1, 10):
                        if (A*1000 + B*100 + C*10 + D) * 9 == (D*1000 + C*100 + B*10 + A):
                            print("{0}{1}{2}{3} *9 = {4}{5}{6}{7}".format(A,B,C,D,D,C,B,A))
                            print("A = {0}, B = {1}, C = {2}, D = {3}".format(A,B, C, D))



def main():
    countNumber = CountNumber()
    countNumber.numAbcd()

if __name__ == '__main__':
    main()