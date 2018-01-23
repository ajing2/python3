#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 22:07
# @Author  : lingxiangxiang
# @File    : test.py


import pdfkit

pdfkit.from_string("hello world", "1.pdf")
pdfkit.from_url("www.baidu.com", "2.pdf")
pdfkit.from_file("hello.html", "3.pdf")