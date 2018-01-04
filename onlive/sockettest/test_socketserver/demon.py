#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 21:00
# @Author  : lingxiangxiang
# @File    : demon.py
#以下的运行环境需要在python2.x的版本上才可以运行，python3不支持
import SimpleHTTPServer
import SocketServer

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
host = "127.0.0.1"
port  = 1111
address = (host, port)
aaa = SocketServer.TCPServer(server_address=address, RequestHandlerClass=Handler)
aaa.serve_forever()