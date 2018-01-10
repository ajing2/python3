#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 12:06
# @Author  : lingxiangxiang
# @File    : test.py
import re
import timeit
print(timeit.timeit(setup='''import re; reg = re.compile('<(?P<tagname>\w*)>.*</(?P=tagname)>')''', stmt='''reg.match('<h1>xxx</h1>')''', number=1000000))
print(timeit.timeit(setup='''import re''', stmt='''re.match('<(?P<tagname>\w*)>.*</(?P=tagname)>', '<h1>xxx</h1>')''', number=1000000))

import re
p = re.compile(r'.\D+\d+')
print(p.findall('one1two2three3four4'))
a = p.finditer('one1two2three3four4')
# 结果：
# ['1', '2', '3', '4']

resutl = p.search('one1two2three3four4')
resutl1 = p.match('one1two2three3four4')
print(resutl)
print(resutl1)
print(resutl.groups())
print(resutl.group(0))
print(resutl.group(1))
print(resutl.group(2))
print(resutl1.groups())
