#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/31 22:06
# @Author  : lingxiangxiang
# @File    : demondatetime.py
from datetime import datetime, timedelta
import time

print(datetime.now())
nowTime = datetime.now()
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)

print(nowTime)
print(type(nowTime))
time1 = nowTime + timedelta(days=1, weeks=-1)

print(nowTime.strftime("%Y-%m-%d"))
print(nowTime.strptime("2017-12-3 22:19:27", "%Y-%m-%d %H:%M:%S"))

t = time.time()
print(t)
m = datetime.fromtimestamp(t)
print(m)
print(type(m))
