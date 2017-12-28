#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 21:09
# @Author  : lingxiangxiang
# @File    : demon2.py
'''九宫格'''

class NinePaper(object):
    def __init__(self):
        print('''
                    _____________
                    |_A_|_B_|_C_|
                    |_D_|_E_|_F_|
                    |_G_|_H_|_I_|
                    A, B, C, D, E, F, G, H, I 必须是1-9数字，且不能重复
                    所有的行，列，对角线的和都为15
        ''')
        self.numbers = list()
        for i in range(1, 10):
            self.numbers.append(i)
        print("numbers = {0}".format(self.numbers))
    def run(self):
        for A in range(1, 10):
            l1 = list()
            l1 += self.numbers
            l1.remove(A)
            for B in l1:
                l2 = list()
                l2 += l1
                l2.remove(B)
                for C in l2:
                    l3 = list()
                    l3 += l2
                    l3.remove(C)
                    for D in l3:
                        l4 = list()
                        l4 += l3
                        l4.remove(D)
                        for E in l4:
                            l5 = list()
                            l5 += l4
                            l5.remove(E)
                            for F in l5:
                                l6 = list()
                                l6 += l5
                                l6.remove(F)
                                for G in l6:
                                    l7 = list()
                                    l7 += l6
                                    l7.remove(G)
                                    for H in l7:
                                        l8 = list()
                                        l8 += l7
                                        l8.remove(H)
                                        for I in l8:
                                            if A+B+C == D+E+F == G+H+I == A+D+G == B+E+H == C+F+I == A+E+I == C+E+G == 15:
                                                print('''
                                            _____________
                                            |_{0}_|_{1}_|_{2}_|
                                            |_{3}_|_{4}_|_{5}_|
                                            |_{6}_|_{7}_|_{8}_|
                                                '''.format(A, B, C, D, E, F, G, H, I))




def main():
    ninePaper = NinePaper()
    ninePaper.run()

if __name__ == '__main__':
    main()