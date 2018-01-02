#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lingxiangxiang

import socket

host = 'www.baidu.com'
port = 80

new_ip = socket.gethostbyname(host)
print('Connect to', host, 'is', new_ip)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((new_ip, port))
    request = "GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n"
    print(type(request))
    s.sendall(request.encode("utf-8"))
    # python3 sendall发送的不是string，而是bytes        python2   要求发送的是string
    reply = s.recv(80960)
    if reply:
        print('ok!')
    else:
        print('on!')
    print(reply)
    s.close()
except socket.error as e:
    print(e)