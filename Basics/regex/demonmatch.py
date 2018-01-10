#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 15:56
# @Author  : lingxiangxiang
# @File    : demonmatch.py
import re

text = "aaahello ajing, hello world"
reg = re.compile(r'hello\s+(.*)\s+hello\s(.*)')
# result = reg.match(text)
result = reg.search(text)

print(result)
print(result.groups())
print(result.group(2))
print(result.groupdict())

