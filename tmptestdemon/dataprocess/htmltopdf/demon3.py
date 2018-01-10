#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 15:32
# @Author  : lingxiangxiang
# @File    : demon3.py

import PyPDF2
import os

#建立一个装pdf文件的数组
pdfFiles = []

for fileName in os.listdir('aming'):    #遍历该程序所在文件夹内的文件
    if fileName.endswith('.pdf'):   #找到以.pdf结尾的文件
        pdfFiles.append(fileName)   #将pdf文件装进pdfFiles数组内

# pdfFiles.sort()     #文件排序
print(pdfFiles)

os.chdir("aming")
pdfWriter = PyPDF2.PdfFileWriter()     #生成一个空白的pdf文件

for fileName in pdfFiles:
    pdfReader = PyPDF2.PdfFileReader(open(fileName,'rb'))   #以只读方式依次打开pdf文件
    for pageNum in range(pdfReader.numPages):
        print(pdfReader.getPage(pageNum))
        pdfWriter.addPage(pdfReader.getPage(pageNum))    #将打开的pdf文件内容一页一页的复制到新建的空白pdf里

pdfOutput = open('combine.pdf','wb')     #生成combine.pdf文件
pdfWriter.write(pdfOutput)               #将复制的内容全部写入combine.pdf
pdfOutput.close()
