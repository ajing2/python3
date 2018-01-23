#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 20:36
# @Author  : lingxiangxiang
# @File    : demon1.py

import requests

url = "https://www.jd.com"
param = {"key1": "hello", "key2": "world"}
r = requests.get(url=url, params=param)
print(r.url)

header = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
r1 = requests.post(url=url, data=param, headers=header)
print(r1.url)

print(r.url)
print(r.text)
print(r.content)
print(r.encoding)
print(r.headers)
print(r.cookies)
print(r.status_code)

s = requests.session()
s.get()
s.post()


