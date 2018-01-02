#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 16:16
# @Author  : lingxiangxiang
# @File    : demon1.py


import socket
import os
from threading import Thread

import time


class SocketServer(object):
    def __init__(self, host, port):
        print("server start, port is 8009!")
        self.host = host
        self.port = port
        self.address = (host, port)
        self.s = None
        self.conn = None
        self.clientAddr = None

    def initSocket(self, listenNum):
        try:
            if isinstance(listenNum, str):
                print("listenNum must is str.")
            if listenNum<1:
                print("listenNum>0")

            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(self.address)
            self.s.listen(listenNum)
        except Exception as e:
            raise e
    def connectClient(self):
        while 1:
            self.conn, self.clientAddr = self.s.accept()
            worker = MultilWorker(self.conn, self.clientAddr)
            worker.start()
            # worker.join()
            # worker.close()
        self.s.close()

class Socketclient(object):
    def __init__(self,host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(self.address)
    def senddata(self):
        name = input("please input your name: ")
        try:
            if len(name)<=0:
                raise("name is None.")
            self.s.sendall(name.encode("utf-8"))
            data = self.s.recv(2048)
            print("name upper is: {0}".format(data))
            time.sleep(5)
            self.s.sendall("close socket!!!".encode('utf-8'))
        except Exception as e:
            raise e


class MultilWorker(Thread):
    def __init__(self, conn, addr):
        super(MultilWorker, self).__init__()
        self.conn = conn
        self.addr = addr
    def run(self):
        print("recv request from {0}".format(self.addr))
        data = self.conn.recv(2048)
        print("the data from client is: {0}".format(data))
        self.conn.sendall(data.upper())



