#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 19:30
# @Author  : lingxiangxiang
# @File    : demonWrite.py

if __name__ == '__main__':
    filename = input("Please input the name of file: ")
    f = open(filename, "w", encoding="utf-8")
    while 1:
        context = input("please input context('EOF' will close file): ")
        if context == "EOF":
            f.close()
            break
        else:
            f.write(context)
            f.write("\n")


    fRead = open(filename, encoding="utf-8")
    readContext = fRead.read()
    print("################start#####################")
    print(readContext)
    print("################end#######################")
    fRead.close()