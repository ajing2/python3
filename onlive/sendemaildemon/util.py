#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 21:19
# @Author  : lingxiangxiang
# @File    : util.py
import codecs

import re

fileName = "message.conf"

def getProperty(property):
    with codecs.open(fileName, encoding="utf-8") as f:
        if property != "message":
            for line in f.readlines():
                if line.startswith("{0} = ".format(property)):
                    value = line.split("{0} = ".format(property))[1]
                    # print(value)
                    return value
        else:
            reg = re.compile(r"message = '''((.*\n)*)'''")
            # print(f.read())
            result = reg.findall(f.read())
            # print(result[0][0])
            return result[0][0]




