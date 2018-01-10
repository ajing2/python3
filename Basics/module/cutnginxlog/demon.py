#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 23:25
# @Author  : lingxiangxiang
# @File    : demon.py
import codecs
from datetime import datetime

import shutil


class CutLog(object):
    def __init__(self):
        self.accessLog = "access.log"
        self.errorLog = "error.log"

    def getToday(self):
        self.nowTime = datetime.now().strftime("%Y-%m-%d")
        self.todayAccessLog = self.nowTime + self.accessLog
        self.todayErrorLog = self.nowTime + self.errorLog

    def renameLog(self):
        shutil.copy(self.accessLog, self.todayAccessLog)
        shutil.copy(self.errorLog, self.todayErrorLog)
        fa = codecs.open(self.accessLog, "w")
        fe = codecs.open(self.errorLog, "w")
        fa.close()
        fe.close()




def main():
    cutLog = CutLog()
    cutLog.getToday()
    cutLog.renameLog()
if __name__ == '__main__':
    main()