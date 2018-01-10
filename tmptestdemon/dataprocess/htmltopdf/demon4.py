#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 15:40
# @Author  : lingxiangxiang
# @File    : demon4.py
#PyPDF2可能会打不开某些pdf文档，也不能提取图片，图表或者其他媒介从PDF文件中。但是它能提取文本从PDF中，转化为字符。
import PyPDF2
import os

os.chdir("aming")
#以二进制方式 读模式打开一个pdf文件
pdfFileObj=open('1.pdf','rb')
#读取pdf文档
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
#返回的是pdf文档的总页数
print(pdfReader.numPages)
#获取单页的内容，页码数从0开始
pageObj=pdfReader.getPage(0)
#
#对于有加密的pdf文档其读对象有属性 isEncrypted
# print(pdfReader.isEncrypted) #若有加密，则属性值为True。直接获取某页的文本内容会报错。
#通过方法decrypt()传递解密密码后可正常获取文本内容,密码以字符串形式传入。
#pdfReader.decrypt('rosebud')