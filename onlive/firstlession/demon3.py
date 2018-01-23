#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 22:14
# @Author  : lingxiangxiang
# @File    : demon9.py
import codecs

import os


class SortPasswd(object):
    def __init__(self):
        self.passwd = "passwd"
        self.newpasswd = "newPasswd"
        self.contextList = list()
        if not os.path.exists(self.passwd):
            print("please download passwd from linux.")
            exit(1)
        print("sort file is :{0}".format(self.passwd))
        print("sorted file is :{0}".format(self.newpasswd))
    def getContextList(self):
        with codecs.open("passwd") as fr:
            self.contextList += sorted(fr.readlines(), key=lambda line:int(line.split(":")[2]), reverse=False)
    def writeContextList(self):
        with codecs.open("new_passwd", "w") as fw:
            fw.writelines(self.contextList)



def main():
    sortpasswd = SortPasswd()
    sortpasswd.getContextList()
    sortpasswd.writeContextList()

if __name__ == '__main__':
    main()