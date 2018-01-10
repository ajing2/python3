#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 23:17
# @Author  : lingxiangxiang
# @File    : classwrapp.py


class startend(object):
    # def __init__(self, func):
    #     self.func = func
    def __init__(self, author):
        self.author = author
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("the author of this project is {0}".format(self.author))
            print("########start####################")
            func(*args, **kwargs)
            print("########end######################")
        return wrapper


# @startend()
@startend("lingxiangxiang")
def hello(name):
    print("hello {0}".format(name))


# hello = starend(hello)
hello("ajing")


