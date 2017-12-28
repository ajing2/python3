#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 22:37
# @Author  : lingxiangxiang
# @File    : testserver.py
from onlive.sockettest.util import ClientSocketTest

if __name__ == '__main__':
    socketClient = ClientSocketTest(host="127.0.0.1", port=9999, type="tcp")
    socketClient.run()