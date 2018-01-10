#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/31 21:18
# @Author  : lingxiangxiang
# @File    : test.py

import hashlib
m2 = hashlib.md5()
src = "ajing".encode("utf-8")
m2.update(src)
print(dir(m2))
print(m2.hexdigest())


from io import StringIO
output = StringIO()
output.write('First line. \n')
output.write('First line22222222222222. \n')
print(output.getvalue())
output.truncate(0)
print(output.getvalue())






from io import BytesIO, StringIO
f = BytesIO()
f.write('hello world'.encode("utf-8"))
f.write('\n'.encode("utf-8"))
f.write('ling xiangxiang'.encode("utf-8"))
print(f.getvalue())
fr = BytesIO('MY NAME IS GOOD!'.encode("utf-8"))
print(fr.read())

