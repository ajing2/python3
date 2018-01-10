#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 17:03
# @Author  : lingxiangxiang
# @File    : demonhashlibStringIO.py

import hashlib

m = hashlib.md5("test".encode("utf-8"))
m.update("ling".encode("utf-8"))
print(m.hexdigest())

from io import StringIO
from io import BytesIO
s = StringIO()
print(s.tell())
s.write("今天你好吗？zxcv zxcdfvxcv\n")
s.write("今天你好吗？aaaaaaa\n")
s.write("今天你好吗？bbbbbbb\n")
s.write("今天你好吗？ccccccc\n")
print(s.tell())
print("################")
print(s.readline())
print(s.getvalue())
print(s.truncate(0))
print(s.getvalue())



abc = BytesIO("saldkjfl\nasdljflasd\nsadfja\n".encode("utf-8"))
print(abc.readline())
print(abc.readline())
print(abc.readline())
print(abc.readline())
print(abc.seek())