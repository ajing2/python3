#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 17:20
# @Author  : lingxiangxiang
# @File    : test.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '18910148469@163.com'
receiver = ['974644081@qq.com', '1414873973@qq.com', 'lingjing@jd.com']
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '18910148469@163.com'
password = 'lingjing2315'

text = '''你好， 
            这是一封自动发送的邮件。 

        www.ustchacker.com 11111111'''
msg = MIMEText(text, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = Header(sender, 'utf-8')
msg['To'] = Header(','.join(receiver), 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
