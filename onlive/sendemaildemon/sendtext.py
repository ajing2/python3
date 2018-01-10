#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 18:26
# @Author  : lingxiangxiang
# @File    : sendtext.py
import codecs
import email.mime.multipart
import email.mime.multipart
import email.mime.text
import os
import smtplib
from email.mime.image import MIMEImage

from onlive.sendemaildemon import getProperty


class SendMail(object):
    def __init__(self):
        self.sendFrom = getProperty("From")
        self.sendTo = getProperty("To").split(",")
        self.content = getProperty("message")
        self.sendCc = getProperty("Cc").split(",")
        self.sendFile = list()
        self.sendImage = list()
        for i in getProperty("File").split(","):
            self.sendFile.append(i.replace("\r\n", ""))
        for j in getProperty("Image").split(","):
            self.sendImage.append(j.replace("\r\n", ""))
        self.msg = None
    def setEmailHeader(self):
        self.msg = email.mime.multipart.MIMEMultipart()
        self.msg['from'] = self.sendFrom
        self.msg['to'] = ";".join(self.sendTo)
        self.msg['cc'] = ";".join(self.sendCc)
        self.msg['subject'] = getProperty("Subject")
    def setMessage(self):
        text = email.mime.text.MIMEText(_text=self.content, _subtype="html")
        self.msg.attach(text)
    def setFile(self):
        for file in self.sendFile:
            if os.path.exists(file):
                with codecs.open(file, 'rb') as f:
                    attr = email.mime.text.MIMEText(str(f.read()), _subtype="html")
                attr["Content-Type"] = 'application/octet-stream'
                attr.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', file))
                self.msg.attach(attr)
            else:
                print("{0} file is not exists!".format(file))
    def setImage(self):
        start = 1
        for image in self.sendImage:
            if os.path.exists(image):
                with codecs.open(image, "rb") as f:
                    attrImage = MIMEImage(f.read())
                attrImage.add_header('Content-ID', '<image{0}>'.format(start))
                self.msg.attach(attrImage)
                start += 1
            else:
                print("{0} image is not exists!".format(image))


    def sendemailLast(self):
        smtp = smtplib.SMTP_SSL()
        smtp.connect('smtp.qq.com', 465)
        smtp.set_debuglevel(1)
        print(self.sendFrom)
        smtp.login(self.sendFrom, '11122233')#你邮箱的密码自己写
        print(self.sendTo)
        smtp.sendmail(from_addr=self.sendFrom, to_addrs=self.sendTo + self.sendCc, msg=self.msg.as_string())
        smtp.quit()

def main():
    sendMail = SendMail()
    sendMail.setEmailHeader()
    sendMail.setMessage()
    sendMail.setFile()
    sendMail.setImage()
    sendMail.sendemailLast()

if __name__ == '__main__':
    main()