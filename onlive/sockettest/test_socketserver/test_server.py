#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 22:16
# @Author  : lingxiangxiang
# @File    : test_server.py
import socketserver


class MyTCPHandle(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{0}:{1} wrote:".format(self.client_address[0], self.client_address[1]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == '__main__':
    host, port = 'localhost', 9999
    address = (host, port)
    server = socketserver.TCPServer(address, MyTCPHandle)
    server.serve_forever()