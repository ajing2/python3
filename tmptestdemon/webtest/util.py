#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 23:07
# @Author  : lingxiangxiang
# @File    : util.py

import socket
import os
from threading import Thread

import time

import paramiko
#
#
# class SocketServerWeb(Thread):
#     def __init__(self, host='0.0.0.0', port=4321):
#         print("server start, port is 8009!")
#         self.host = host
#         self.port = port
#         self.address = (host, port)
#         self.s = None
#         self.conn = None
#         self.clientAddr = None
#         self.initSocket()
#
#     def initSocket(self, listenNum=5):
#         try:
#             if isinstance(listenNum, str):
#                 print("listenNum must is str.")
#             if listenNum<1:
#                 print("listenNum>0")
#
#             self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             self.s.bind(self.address)
#             self.s.listen(listenNum)
#         except Exception as e:
#             raise e
#     def connectClient(self):
#         while 1:
#             conn, clientAddr = self.s.accept()
#             worker = MultilWorker(conn, clientAddr)
#             worker.start()
#             # worker.join()
#             # worker.close()
#         self.s.close()
#
#
#
# class MultilWorker(Thread):
#     def __init__(self, conn, addr):
#         super(MultilWorker, self).__init__()
#         self.conn = conn
#         self.addr = addr
#
#     def InitParmiko(self, data={}):
#         self.client = paramiko.SSHClient()
#         self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         self.client.connect(hostname=data["host"], port=data["port"], username=data["username"], password=data["password"])
#
#     def establish(self, term="xterm"):
#         self._shell = self.client.invoke_shell(term)
#         self._shell.setblocking(0)
#         self._id = self._shell.fileno()
#         # IOLoop.instance().register(self)
#         # IOLoop.instance().add_future(self.trans_back())
#         # IOLoop.instance().add_future(self.trans_back())
#
#     def run(self):
#         stat = 1
#         while 1:
#             cmd = input("{0}>> ".format(self.host))
#             if cmd:
#                 stat = 1
#                 stdin, stdout, stderr = self.client.exec_command(cmd)
#                 for std in stdout.readlines():
#                     print(std)
#             else:
#                 stat += 1
#                 time.sleep(60)
#                 if stat == 5:
#                     break



class WebServer(Thread):
    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("127.0.0.1", 4321))
        server.listen(5)
        while 1:
            try:
                conn, clientAddr = server.accept()
                worker = MWorker(conn, clientAddr)
                worker.start()
            except:
                print('websocket connection timeout!')
        server.close()


class MWorker(Thread):
    def __init__(self, conn, clientAddr):
        super(MWorker, self).__init__()
        self.conn = conn
        self.clientAddr = clientAddr

    def connect(self, data):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=data["host"], port=data["port"], username=data["username"], password=data["passwd"])
        return client
    def run(self):
        try:
            data = self.conn.recv(2048)
            if data:
                client = self.connect(data)
                if not client:
                    exit()
        except Exception as e:
            print(e)
            raise e
            self.conn.close()
        while 1:
            cmd = self.conn.recv(1024)
            stdin, stdout, stderr = client.exec_command(cmd)
            cmdresult = stdout.read()
            self.conn.sendall(cmdresult)
        self.conn.close()




