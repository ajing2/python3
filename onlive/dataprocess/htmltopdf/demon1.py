#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 22:07
# @Author  : lingxiangxiang
# @File    : demon1.py
'''爬虫阿铭linux教程，保存为本地的pdf文件'''
# 需要知道三招教你做人
# pdfkit.from_string("hello world", "1.pdf")
# pdfkit.from_url("www.baidu.com", "2.pdf")
# pdfkit.from_file("hello.html", "3.pdf")
import re

import os

import pdfkit
import requests


if not os.path.exists("aminglinux"):
    os.mkdir("aminglinux")
os.chdir("aminglinux")

url = "http://www.apelearn.com/study_v2/"
s = requests.session()
text = s.get(url).text
print(text)
reg = re.compile(r'<li class="toctree-l1"><a class="reference internal" href="(.*)">.*</a></li>')
result = reg.findall(text)
res = list(set(result))
pdfUrl = "http://www.apelearn.com/study_v2/"
for i in res:
    url = "{0}{1}".format(pdfUrl, i)
    pdfFileName = i.replace("html", "pdf")
    print(pdfFileName)
    try:
        pdfkit.from_url(url, pdfFileName)
    except:
        continue



