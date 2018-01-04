#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 10:07
# @Author  : lingxiangxiang
# @File    : demon1.py
import email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

import os

sender = '18910148469@163.com'
receivers = '974644081@qq.com'
subject = 'python test sendmail'
smtpserver = 'smtp.163.com'
username = '18910148469@163.com'
password = 'lingjing2315'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers
message['Subject'] = subject

message.attach(MIMEText(_text='<h1>大家好：</h1>这个是正文', _subtype='plain', _charset='utf-8'))



server = smtplib.SMTP()
server.connect(smtpserver, '25')
server.login(username, password)
server.sendmail(sender, receivers, message.as_string())
server.quit()
