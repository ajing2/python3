#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 15:22
# @Author  : lingxiangxiang
# @File    : demon1.py


import pdfkit
pdfkit.from_url('http://google.com', 'out1.pdf')
pdfkit.from_file("test.html", "out2.pdf")
pdfkit.from_string("hello ajing", "out3.pdf")

