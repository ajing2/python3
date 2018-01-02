#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 14:00
# @Author  : lingxiangxiang
# @File    : client.py
from onlive.sockettest.socketthread.demon1 import Socketclient

host = '127.0.0.1'
port = 8009
server  = Socketclient(host=host, port=port)
server.senddata()
