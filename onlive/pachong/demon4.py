#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 21:52
# @Author  : lingxiangxiang
# @File    : demon4.py

# python2
# import urllib.urlopen(url)
# import urllib2
# urllib2.Request
# data = urllib.encode(data)
# data   key1=hello&key2=world
'''python3  urllib'''
from urllib import parse

data = {"key1": "hello", "key2": "world"}

# python3
import urllib.request

url = "https://www.qiushibaike.com/"
ndata = parse.urlencode(data)
print(ndata)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode("utf-8"))