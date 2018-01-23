#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 20:49
# @Author  : lingxiangxiang
# @File    : demon6.py
import codecs
from urllib import request

jpg = 'http://img1.gtimg.com/ninja/1/2017/05/ninja149496152065814.jpg'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

req = request.Request(url=jpg, headers=headers)
res = request.urlopen(req)
context = res.read()
with codecs.open("test.jpg", 'wb') as f:
    f.write(context)


request.urlretrieve(jpg, "aaa.jpg")
