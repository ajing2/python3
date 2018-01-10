#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 15:06
# @Author  : lingxiangxiang
# @File    : testjson.py
import codecs

import re

text = None
with codecs.open("json.txt", encoding="utf-8") as f:
    text = f.read()
reg = re.compile(r'(skuid)":"(\d+)",')
result = reg.search(text)
print(result)
print(result.groups())
print(reg.findall(text))

