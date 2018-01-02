#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 20:43
# @Author  : lingxiangxiang
# @File    : httpclient.py
import socket

host = "www.baidu.com"
port = 80

ip = socket.gethostbyname(host)
print(ip)
print("connect server ip = {0}".format(ip))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.sendall("GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n".encode("utf-8"))

# python2  s.sendall 必须是字符串，   python3  sendall  必须是字节
data = s.recv(2048)
print(data)
