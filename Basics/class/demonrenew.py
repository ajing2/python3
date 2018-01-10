#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 21:01
# @Author  : lingxiangxiang
# @File    : demonrenew.py

class A(object):
    def __init__(self, id = "A"):
        self.id = id
        print("my role is parent.")
    def run(self, name = "parent"):
        print("父类run: {0}".format(name))
    def start(self):
        print("父类  start")
class B(A):
    # def __init__(self, id):
    #     self.id = id
    #     print("my name is {0}".format(id))
    def run(self, role="parent"):
        print("子类run")
        super(B, self).run(name=role)
b = B("B")
b.run()
b.start()