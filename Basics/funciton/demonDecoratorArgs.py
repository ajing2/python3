#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 16:37
# @Author  : lingxiangxiang
# @File    : demonDecoratorArgs.py

def startend(aothor):
    def a(func):
        def start(name):
            print("the author of thie project is {0}".format(aothor))
            print("###############start##############")
            func(name)
            print("###############end################")
        return start
    return a

@startend("lingxiangxiang")
def hello(name):
    print("hello {0}".format(name))

# hello = startend("lingxiangxinag")(hello)
# a = startend("lingxiangxiang")
# hello = a(hello)
hello("ajing")