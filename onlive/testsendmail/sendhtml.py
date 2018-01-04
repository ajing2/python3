#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 15:36
# @Author  : lingxiangxiang
# @File    : sendhtml.py

import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.image import MIMEImage

import os
# from email import encoders, MIMEImage

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '18910148469@163.com'
msg['to'] = '974644081@qq.com;1414873973@qq.com;lingjing@jd.com'
msg['subject'] = 'ajing1111'
content = '''
    <h1>老师好</h1>
    你好， 
            这是一封自动发送的邮件。 

        www.ustchacker.com hello
    <html>
<body>
<h1>hello world</h1>
<p>
图片演示：<br><img src = 'cid:image1'></br>
</p>
</body>
</html>
'''
txt = email.mime.text.MIMEText(_text=content, _subtype="html")
msg.attach(txt)

#############
attfile = 'test.py'
basename = os.path.basename(attfile)
fp = open(attfile, 'rb')
att = email.mime.text.MIMEText(fp.read(), 'html', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', basename))#three-tuple of (charset, language, value),
# encoders.encode_base64(att)
msg.attach(att)
##########

#################
img = "1.jpg"
fimg = open(img, "rb")
imgattr = MIMEImage(fimg.read())
fimg.close()
imgattr.add_header('Content-ID', '<image1>')
msg.attach(imgattr)
################

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('18910148469@163.com', 'LingJing2315')
smtp.sendmail(from_addr='18910148469@163.com', to_addrs=['974644081@qq.com', '1414873973@qq.com', 'lingjing@jd.com'], msg=msg.as_string())
smtp.quit()
