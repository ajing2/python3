#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 22:27
# @Author  : lingxiangxiang
# @File    : test_client.py
import socket
import socketserver

host, port = "localhost", 9999
data = "hello world"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, port))
    sock.sendall(data.encode("utf-8"))
    recv_data = sock.recv(1024)
except Exception as e:
    raise e
finally:
    sock.close()

print("sent: {0}".format(data))
print("recv: {0}".format(recv_data))
