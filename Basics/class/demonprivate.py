#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 21:52
# @Author  : lingxiangxiang
# @File    : demonprivate.py

class A(object):
    def __init__(self, name, age):
        self.__author = "lingxiangxiang"
        self.name = name
        self.age = age
    def getAuthor(self):
        return self.__author
    def setAuthor(self, author):
        self.__author = author

if __name__ == '__main__':
    a = A("张三", 18)
    print(a.getAuthor())
    a.setAuthor("ajing")
    print(a.getAuthor())

