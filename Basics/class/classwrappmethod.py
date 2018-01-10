#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 19:21
# @Author  : lingxiangxiang
# @File    : classwrappmethod.py
'''区分@staticmethod, @clasmethod, 普通方法的区别'''

class A(object):
    def func(self):
        print("hello func.")
        print("#####################################")

    @classmethod
    def classFunc(cls, name):
        print("hello #######{0} ######clsssmethod".format(cls))
        cls.name = name
        print("hello {0}".format(cls.name))

    @staticmethod
    def staticFunc():
        print("this class is statimethod")
        A.id = "lignxiangxiang"
        print("id = {0}".format(A.id))


a = A()
a.func()
# a.classFunc()
# a.staticFunc()
A.staticFunc()
A.classFunc("ajing")
print(A.name)
print(A.id)
# A.func()