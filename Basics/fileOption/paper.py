#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 9:53
# @Author  : lingxiangxiang
# @File    : paper.py
'''九宫格
            ____________
            |_A_|_B_|_C_|
            |_D_|_E_|_F_|
            |_G_|_H_|_I_|

'''

number = list()
for i in range(1,10):
    number.append(i)




for A in number:
    a = list()
    for i in range(1, 10):
        a.append(i)
    # m = number
    a.remove(A)
    for B in a:
        b = list()
        for i in a:
            b.append(i)
        b.remove(B)
        for C in b:
            c = list()
            for i in b:
                c.append(i)
            c.remove(C)
            for D in c:
                d = list()
                for i in c:
                    d.append(i)
                d.remove(D)
                for E in d:
                    e = list()
                    for i in d:
                        e.append(i)
                    e.remove(E)
                    for F in e:
                        f = list()
                        for i in e:
                            f.append(i)
                        f.remove(F)
                        for G in f:
                            g = list()
                            for i in f:
                                g.append(i)
                            g.remove(G)
                            for H in g:
                                h = list()
                                for i in g:
                                    h.append(i)
                                h.remove(H)
                                for I in h:
                                    if (A+B+C) == (D+E+F) == (G+H+I) == (A+D+G) == (B+E+H) == (C+F+I) == (A+E+I) == (C+E+G) == 15:
                                        print('''
                                            _____________
                                            |_{0}_|_{1}_|_{2}_|
                                            |_{3}_|_{4}_|_{5}_|
                                            |_{6}_|_{7}_|_{8}_|
                                        '''.format(A, B, C, D, E, F, G, H, I))
# b = a
# a, b  指向的是通一个内存地址, 对b进行删除元素的时候，a列表页随着删除