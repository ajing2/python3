#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 22:51
# @Author  : lingxiangxiang
# @File    : demonjson.py
import codecs
import json
import urllib.request

url = 'http://qwd.jd.com/fcgi-bin/qwd_searchitem_ex?g_tk=971960084&skuid=10657305771%7C11203636763%7C10571390914%7C13109264362%7C10386721898%7C12140975201%7C10439177256%7C13612561077%7C10171375206%7C13160174542%7C11641043874%7C13160308174%7C13618848172%7C13521003503%7C11062203238%7C10417123209%7C11712536222%7C12977266053%7C11287630528%7C11794389616'
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
result = res.read()
print(result.decode("utf-8"))
print(type(result))
m = json.loads(result)
print(type(m))
print(m['sku'][1]["skuid"])
print(m['sku'][0]["title"])



d = dict(a=1, b=2, c=3, d=4)
f = codecs.open("json.txt", "w")
json.dump(d, f)
f.close()
mm = json.dumps(d)
print(mm)
print(type(mm))



fr = open("json.txt", "r")
aaa = json.load(fr)
print(aaa)
print(type(aaa))