#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 22:15
# @Author  : lingxiangxiang
# @File    : demon5.py
'''python2 示例的urllib和urllib2'''

import urllib2
import urllib
data = {"key1": "hello", "key2": "world"}
ndata = urllib.urlencode(data)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url = "https://www.qiushibaike.com/"
req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req)
print(res.read())