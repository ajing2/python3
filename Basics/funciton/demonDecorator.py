#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 14:41
# @Author  : lingxiangxiang
# @File    : demonDecorator.py
#
# def hello():
#     print("hello world")
#
# # hello()
#
#
# def test():
#     print("#################start##################")
#     # print("hello world")
#     hello()
#     print("#################end####################")
# # test()
#
#
#
# print(callable(hello))
#
#
# a = hello
# a()#就相当于执行了hello()


def startend(func):
    def start():
        print("###############start##############")
        func()
        print("###############end################")
    return start

@startend
def hello():
    print("hello world")

# hello = startend(hello)
# hello()

# hello()
