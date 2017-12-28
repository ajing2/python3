#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 22:37
# @Author  : lingxiangxiang
# @File    : testserver.py
from onlive.sockettest.util import SocketServerTest

if __name__ == '__main__':
    socketServer = SocketServerTest(host="0.0.0.0", port=9999, type="tcp", backlog=5)
    socketServer.run()