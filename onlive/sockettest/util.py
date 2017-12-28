#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 22:11
# @Author  : lingxiangxiang
# @File    : util.py
import socket

import time


class InitSocketTest(object):
    def __init__(self, host, port, type):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.type = type
        self.s = None
        self.creatsocket()

    def creatsocket(self):
        if self.type.upper() == "TCP":
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif self.type.upper == "UDP":
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print("you must input the InitSocket(type) is 'UDP|TCP' ")

class SocketServerTest(InitSocketTest):
    def __init__(self, host, port, type,  backlog):
        self.backlog = backlog
        super(SocketServerTest, self).__init__(host, port, type)
        self.clientAddress = None

    def run(self):
        self.s.bind(self.address)
        self.s.listen(self.backlog)
        print("server starting…………")
        conn, self.clientAddress = self.s.accept()
        print("accept connect from {0}".format(self.clientAddress))
        for i in range(1, 10):
            conn.sendall("i = {0}".format(str(i)).encode("utf-8"))
        self.s.close()

class ClientSocketTest(InitSocketTest):
    def run(self):
        self.s.connect(self.address)
        stat = 1
        while 1:
            data = self.s.recv(2048)
            if len(data)>0:
                stat = 1
                print(data.decode("utf-8"))
            else:
                stat += 1
                time.sleep(1)
                if stat == 5:
                    break



