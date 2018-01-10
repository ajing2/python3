#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 16:03
# @Author  : lingxiangxiang
# @File    : demonfindall.py
import urllib.request

import re


class GetSkuid(object):
    def __init__(self, url):
        self.url = url
        self.text = None
        self.reg = None
    def gettext(self):
        req = urllib.request.Request(url=self.url)
        self.text = urllib.request.urlopen(req).read()
    def regexSkuid(self):
        self.reg = re.compile(r'((skuid)":"(\d+)",)')
        self.result = self.reg.findall(self.text.decode("utf-8"))
        print(self.result)




def main():
    url = 'http://qwd.jd.com/fcgi-bin/qwd_searchitem_ex?g_tk=971960084&skuid=10657305771%7C11203636763%7C10571390914%7C13109264362%7C10386721898%7C12140975201%7C10439177256%7C13612561077%7C10171375206%7C13160174542%7C11641043874%7C13160308174%7C13618848172%7C13521003503%7C11062203238%7C10417123209%7C11712536222%7C12977266053%7C11287630528%7C11794389616'
    getskuid = GetSkuid(url=url)
    getskuid.gettext()
    getskuid.regexSkuid()

if __name__ == '__main__':
    main()