#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 17:35
# @Author  : lingxiangxiang
# @File    : nginxconfigcut.py
import codecs

import re

import os


class CutNginxConf(object):
    def __init__(self, filename):
        self.filename = filename
        self.coding = "utf-8"
        self.regUptream = re.compile(r'(upstream\s+(\S+)\s+{(\s+server\s+.*\n)+})')
        self.regLocation = re.compile(r'(location\s+/(\S+)/\s+{\s+proxy_next_upstream\s+[^}]+})')
        self.pwddir = os.getcwd()

    def cutUpstream(self):
        os.chdir(self.pwddir)
        with codecs.open(self.filename, encoding=self.coding) as fuptream:
            if not os.path.exists("upstream"):
                os.mkdir("upstream")
            os.chdir("upstream")
            result = self.regUptream.findall(fuptream.read())
            for upstream in result:
                upstremFile = "{0}.upstream.conf".format(upstream[1].split(".")[0])
                with codecs.open(upstremFile, "w") as f:
                    f.write(upstream[0])

    def cutLocation(self):
        os.chdir(self.pwddir)
        with codecs.open(self.filename,encoding=self.coding) as flocation:
            if not os.path.exists("locaiton"):
                os.mkdir("location")
            os.chdir("location")
            resutl = self.regLocation.findall(flocation.read())
            for location in resutl:
                filename = "{0}.location.conf".format(location[1])
                with open(filename, "w") as f:
                    f.write(location[0])



def main():
    cutNginxConf = CutNginxConf("test.conf")
    cutNginxConf.cutUpstream()
    cutNginxConf.cutLocation()


if __name__ == '__main__':
    main()