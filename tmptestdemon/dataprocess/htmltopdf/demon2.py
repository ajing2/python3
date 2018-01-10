#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 15:28
# @Author  : lingxiangxiang
# @File    : demon2.py


import codecs
import os
import sys

import pdfkit
import requests

base_url = 'http://www.apelearn.com/study_v2/'
if not os.path.exists("aming"):
    os.mkdir("aming")

os.chdir("aming")
s = requests.session()

for i in range(1, 27):
    url = base_url + 'chapter' + str(i) + '.html'
    print(url)
    file = str(i) + '.pdf'
    print(file)
    config = pdfkit.configuration(wkhtmltopdf=r"D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    try:
        pdfkit.from_url(url, file)
    except:
        continue
