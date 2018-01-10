#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 14:46
# @Author  : lingxiangxiang
# @File    : demon1.py
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfparser import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
#获取文档对象，你把algorithm.pdf换成你自己的文件名即可。
fp=open("test.pdf","rb")
#创建一个与文档相关联的解释器
parser=PDFParser(fp)
#PDF文档对象,提供密码初始化，没有就不用带password参数。
doc=PDFDocument()

parser.set_document(doc)
doc.set_parser(parser)

doc.initialize()
#检查文件是否允许文本提取
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
#链接解释器和文档对象
# parser.set_document(doc)
#doc.set_paeser(parser)
#初始化文档
#doc.initialize("")
#创建PDF资源管理器对象来存储共享资源
resource=PDFResourceManager()
#参数分析器
laparam=LAParams()
#创建一个聚合器
device=PDFPageAggregator(resource, laparams=laparam)
#创建PDF页面解释器
interpreter=PDFPageInterpreter(resource,device)
#使用文档对象得到页面集合
for page in doc.get_pages():
  #使用页面解释器来读取
  interpreter.process_page(page)
  #使用聚合器来获取内容
  layout=device.get_result()
  for out in layout:
    if hasattr(out, "get_text"):
      print(out.get_text())
