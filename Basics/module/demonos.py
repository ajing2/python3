#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 14:01
# @Author  : lingxiangxiang
# @File    : demonos.py


# cd   pwd   ls   ifconfig

import os

print(os.name)

# os.system("ipconfig |findstr atap")
a = os.popen("ipconfig |findstr atap")
print(type(a))
print(a.read())

# print(os.getcwd())
# print(os.chdir("D:"))
# print(os.getcwd())

# if not os.path.exists("ajing"):
#     os.mkdir("ajing")