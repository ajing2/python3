#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:22
# @Author  : lingxiangxiang
# @File    : server.py
from onlive.sockettest.socketthread.demon1 import SocketServer

host = '0.0.0.0'
port = 8009
server  = SocketServer(host=host, port=port)
server.initSocket(listenNum=2)
server.connectClient()
