#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 21:02
# @Author  : lingxiangxiang
# @File    : demon8.py
import requests

url = "http://www.hao123.com"
s = requests.session()
r = s.get(url)
print(r.cookies)
for cook in r.cookies:
    print(cook.name)
    print(cook.value)
    print(cook.domain)
    print(cook.path)
    print(cook.expires)
    print('#########################')