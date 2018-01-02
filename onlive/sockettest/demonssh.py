#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 20:57
# @Author  : lingxiangxiang
# @File    : demonssh.py
import socket

import time

if __name__ == '__main__':
    host = "192.168.48.131"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    stat = 1
    while 1:
        cmd = input("{0}>>> ".format(host))
        if cmd.lower() == "exit":
            exit()
        if not cmd:
            continue
        s.sendall(cmd.encode("utf-8"))
        data = s.recv(2048)
        redata = data.decode("utf-8").replace("\n", "\r\n")
        # print(type(data))
        if len(data)>0:
            stat = 1
            print("{0}".format(redata))
        else:
            stat += 1
            time.sleep(1)
            if stat == 5:
                break
