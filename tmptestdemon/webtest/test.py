#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 23:11
# @Author  : lingxiangxiang
# @File    : test.py

class A(object):
    def __init__(self):
        print("create AAAAAAAA")
    @staticmethod
    def hello():
        print("hello world")

a = A()
a.hello()