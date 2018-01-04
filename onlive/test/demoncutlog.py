#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 21:00
# @Author  : lingxiangxiang
# @File    : demoncutlog.py
import codecs
from datetime import datetime

import os

import shutil


class CutLog(object):
    def __init__(self):
        self.nginxAccessLog = "access.log"
        self.nginxErrorLog = "error.log"
        # self.getTodayLog()
        # self.renameLog()

    def getTodayLog(self):
        self.nowTime = datetime.now().strftime("%Y-%m-%d")
        self.todayAccessLog = self.nowTime + self.nginxAccessLog
        self.todayErrorLog = self.nowTime + self.nginxErrorLog

    def renameLog(self):
        shutil.copy(self.nginxAccessLog, self.todayAccessLog)
        shutil.copy(self.nginxErrorLog, self.todayErrorLog)
        fa = codecs.open(self.nginxAccessLog, "w")
        fe = codecs.open(self.nginxErrorLog, "w")
        fa.close()
        fe.close()

def main():
    cutlog = CutLog()
    cutlog.getTodayLog()
    cutlog.renameLog()

if __name__ == '__main__':
    main()