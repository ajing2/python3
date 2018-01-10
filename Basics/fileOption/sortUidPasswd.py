#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 21:45
# @Author  : lingxiangxiang
# @File    : sortUidPasswd.py
'''对/etc/passwd 的第三列 uid进行排序，然后生成排序后的新文件'''
import codecs

file = "passwd"
sortfile = "sortpasswd.txt"
filecontext = []
sortuid = []

with codecs.open(sortfile, 'wb') as fsort:
    with codecs.open(file, encoding="utf-8") as f:
        filecontext += f.readlines()
        for line in filecontext:
            sortuid.append(int(line.split(":")[2]))
        sortuid.sort()
        for uid in sortuid:
            for line in filecontext:
                if str(uid) == line.split(":")[2]:
                    print(line)
                    fsort.write(line.encode("utf-8"))#line.encode("utf-8")把字符串转换成