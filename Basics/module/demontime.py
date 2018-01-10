#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/31 21:29
# @Author  : lingxiangxiang
# @File    : demontime.py

import time
import datetime

print("##"*10)
# time.sleep(2)
print("##"*10)
print(time.time())

print(time.localtime())
print(time.mktime(time.localtime()))

print(time.asctime())
print(time.ctime())

print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strptime("2015-12-31 21:39:11", "%Y-%m-%d %H:%M:%S"))

print(time.strftime("%c"))



