#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 21:06
# @Author  : lingxiangxiang
# @File    : demon9.py
import requests

url = "http://2017.ip138.com/ic.asp"
# s = requests.session()
# r = s.get(url=url)
# print(r.encoding)
# r.encoding = "gb2312"
# print(r.text)
# print(result)

########代理

proxies = {"http": "http://122.225.17.123:8080"}
r1 = requests.get(url=url, proxies=proxies)
r1.encoding = "gbk"
print(r1.text)

