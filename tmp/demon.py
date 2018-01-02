#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 10:05
# @Author  : lingxiangxiang
# @File    : demon.py
import datetime
import hashlib
import random
import time
from io import StringIO

f = StringIO()
output = StringIO('HELLO \nWORLDL \nLING \nJING\n')
f.write("hello world")
print(f.read())
print(f.getvalue())
print(output.read())
print(output.getvalue())


print(time.time())
# time.sleep(1)
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print(time.strftime("%Y-%m-%d",time.localtime()))
print(time.asctime())
a = "Thu Aug 18 14:07:27 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
print(time.ctime())
print(time.asctime())
print(time.mktime(time.localtime()))
print(datetime.datetime.now())
print(random.uniform(10, 20))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list1, 5)
print(slice)

md_five = hashlib.md5(bytes('898oaFs09f',encoding="utf-8"))
print(md_five)
md_five.update(b'Hello World')
mm = md_five.digest()
print(mm)
print(type(mm))
result = md_five.hexdigest()
print(type(result))
print(result)

# !/usr/bin/env python
# -*- coding:utf-8 -*-
import getpass

user = input("请输入用户名:")

# 将用户输入的内容赋值给变量pwd
pwd = getpass.getpass("请输入密码:")
print(user)
print(pwd)
