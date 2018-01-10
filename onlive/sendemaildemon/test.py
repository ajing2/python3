#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 21:39
# @Author  : lingxiangxiang
# @File    : test.py
import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '18910148469@163.com'
msg['to'] = '1414873973@qq.com'
# a = '583998580@qq.com,251642766@qq.com,wxp997@189.cn,879129517@qq.com,120524261@qq.com,1210640219@qq.com,376176572@qq.com,liujie475030894@126.com,287990400@qq.com,1069231646@qq.com,zhangxun_1994@126.com,327357283@qq.com,978951161@qq.com,114653379@qq.com,286577399@qq.com,609998938@qq.com,1032399080@qq.com,381590516@qq.com,974644081@qq.com'
# sendtoname = a.split(",")
msg['subject'] = 'ajing'
msg['cc'] = '974644081@qq.com'
content = '''
    <h1>老师好</h1>
'''
txt = email.mime.text.MIMEText(_text=content, _subtype="html")
msg.attach(txt)

smtp = smtplib.SMTP_SSL()
smtp.connect('smtp.163.com', '465')
smtp.login('18910148469@163.com', 'LingJing2315')
smtp.sendmail(from_addr='18910148469@163.com', to_addrs=['1414873973@qq.com'] + ['974644081@qq.com'], msg=msg.as_string())
smtp.quit()