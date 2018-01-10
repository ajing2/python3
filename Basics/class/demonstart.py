#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 17:21
# @Author  : lingxiangxiang
# @File    : demonstart.py

class Student(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        print("欢迎创建创建Stduent对象！")
        self.dns = None
        self.run()
    def run(self):
        print(self.name)

student = Student(111, "ling")
# student.run()