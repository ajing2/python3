#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 22:36
# @Author  : lingxiangxiang
# @File    : test.py

import json
a = dict(hello='你好')
print(a)
print(a["hello"])
n1 = json.dumps(a)
n2 = json.dumps(a, ensure_ascii=False)
print(type(n1))
print(n1)
print(type(n2))
print(n2)