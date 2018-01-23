#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 21:13
# @Author  : lingxiangxiang
# @File    : demon8.py

import PyPDF2
import os

pdfList = list()
'''遍历所有的pdf文件到pdfList列表中'''
# for each in os.listdir("aminglinux"):
#     pdfList.append(each)
for i in range(1, 27):
    pdfList.append("chapter{0}.pdf".format(i))
print(pdfList)
os.chdir("aminglinux")
pdfWrite = PyPDF2.PdfFileWriter()
for pdf in pdfList:
    pdfReader = PyPDF2.PdfFileReader(open(pdf, "rb"))
    print("{0} have {1} pages.".format(pdf, pdfReader.numPages))
    for page in range(pdfReader.numPages):
        pdfWrite.addPage(pdfReader.getPage(page))

f = open("aminglinux.pdf", "wb")
pdfWrite.write(f)
f.close()
