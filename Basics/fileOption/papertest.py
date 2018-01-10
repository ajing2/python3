#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 8:35
# @Author  : lingxiangxiang
# @File    : papertest.py
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
    for B in number:
        for C in number:
            for D in number:
                for E in number:
                    for F in number:
                        for G in number:
                            for H in number:
                                for I in number:
                                    s = set()
                                    s.add(A)
                                    s.add(B)
                                    s.add(C)
                                    s.add(D)
                                    s.add(E)
                                    s.add(F)
                                    s.add(G)
                                    s.add(H)
                                    s.add(I)
                                    if (A+B+C) == (D+E+F) == (G+H+I) == (A+D+G) == (B+E+H) == (C+F+I) == (A+E+I) == (C+E+G) == 15 and len(s) == 9:
                                        print('''
                                            _____________
                                            |_{0}_|_{1}_|_{2}_|
                                            |_{3}_|_{4}_|_{5}_|
                                            |_{6}_|_{7}_|_{8}_|
                                        '''.format(A, B, C, D, E, F, G, H, I))