#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Time    : 2017/12/23 19:56
# @Author  : lingxiangxiang
# @File    : codeType.py
'''python 2环境    '''
# import sys
# reload(sys)
# print(sys.getdefaultencoding())
# sys.setdefaultencoding("utf-8")
# print(sys.getdefaultencoding())

a = u"你好"
print(type(a))

s = "你好吗"
print(s.decode("utf-8"))
print(s)
print(type(s))
l = [1, 2, 3, 4, "大家好才是真的好，广州好迪"]
print(l[4].decode("utf-8"))
print(l)


m = "中文"
print(m.decode("utf-8").encode("gbk"))