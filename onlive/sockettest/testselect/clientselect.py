#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 22:22
# @Author  : lingxiangxiang
# @File    : clientselect.py

import socket, select, string, sys
import time

# main function
if __name__ == "__main__":
    host = "192.168.48.131"
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host, port))
    except:
        print('Unable to connect')
        sys.exit()
    print('Connected to remote host. Start sending messages')

    while 1:
        rlist = [sys.stdin, s]
        read_list, write_list, error_list = select.select(rlist, [], [])
        for sock in read_list:
            if sock == s:
                data = sock.recv(2048)
                if not data:
                    continue
                else:
                    sys.stdout.write(data)
            else:
                msg = raw_input("我说： ")
                s.sendall(msg)