#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 22:24
# @Author  : lingxiangxiang
# @File    : testyagmail.py

# pip install yagmail
import yagmail
yag=yagmail.SMTP(user='18910148469@163.com',password='LingJing2315',host='smtp.163.com', port='465' )
yag.send(to='974644081@qq.com',subject="test",contents='this is a testing',attachments='test.py',cc='1414873973@qq.com')
