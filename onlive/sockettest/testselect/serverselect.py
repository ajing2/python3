#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 22:04
# @Author  : lingxiangxiang
# @File    : serverselect.py
import socket

import select


class SelectServer(object):
    def __init__(self, host, port, backlog):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.backlog = backlog
        self.server = None
        self.socketList = list()

    def _initSocket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)
        self.server.listen(self.backlog)
        self.socketList.append(self.server)
        print("chat room has start!")
        while 1:
            rlist, wlist, elist = select.select(self.socketList, [], [])
            for r in rlist:
                if r == self.server:
                    serverConn, clienAddr = self.server.accept()
                    self.socketList.append(serverConn)
                    print("{0}进入了房间".format(clienAddr))
                    self.broadcast(r, "{0}进入了房间".format(clienAddr))
                else:
                    try:
                        data = r.recv(2048)
                        if data:
                            print("{0}: {1}".format(clienAddr, data))
                            self.broadcast(r, "{0}: {1}".format(clienAddr, data))
                    except Exception as e:
                        self.broadcast(r, "{0}下线".format(clienAddr))
                        print("{0}下线".format(clienAddr))
                        r.close()
                        self.socketList.remove(r)

        self.server.close()

    def broadcast(self, r, data):
        for i in self.socketList:
            if i != r and i != self.server:
                try:
                    i.sendall(data)
                except:
                    i.close()
                    self.socketList.remove(i)



def main():
    selectServer = SelectServer(host="127.0.0.1", port=4321, backlog=5)
    selectServer._initSocket()

if __name__ == '__main__':
    main()
