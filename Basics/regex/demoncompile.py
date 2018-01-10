#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 15:22
# @Author  : lingxiangxiang
# @File    : demoncompile.py

import timeit
import re
text = '<h1>xxx</h1>'
reg = re.compile(r'<(?P<tagname>\D+\w*)>.*</(?P=tagname)>',flags=re.I )
result = reg.match('<h1>xxx</h1>')
# match  只匹配一次，而且是从开头开始匹配，如果匹配到，就返回，如果匹配不到，返回None
# search 只匹配一次，从开头开始匹配，如果匹配如果，重新从而第二个开始字符开始匹配
print(result)
print(result.groups())
#
print(timeit.timeit(setup='''import re; reg = re.compile('<(?P<tagname>\D+\w*)>.*</(?P=tagname)>')''', stmt='''reg.match('<h1>xxx</h1>')''', number=1000000))
print(timeit.timeit(setup='''import re''', stmt='''re.match('<(?P<tagname>\D+\w*)>.*</(?P=tagname)>', '<h1>xxx</h1>')''', number=1000000))


