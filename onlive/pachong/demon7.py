#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 21:07
# @Author  : lingxiangxiang
# @File    : demon7.py


from urllib import request

url = 'http://2017.ip138.com/ic.asp'
proxy = request.ProxyHandler({"http": "180.110.4.68:3128"})
opener = request.build_opener(proxy)
request.install_opener(opener)
text = opener.open(url).read()
print(type(text))
print(text.decode("gbk"))