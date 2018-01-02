#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 22:12
# @Author  : lingxiangxiang
# @File    : demonparmiko.py

import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 上面是用来设置known-host
host = "192.168.48.131"
port = 22
username = "root"
passwd = "123456"
client.connect(hostname=host, port=port, username=username, password=passwd)
stat = 1
while 1:
    cmd = input("{0}>> ".format(host))
    if cmd:
        stat = 1
        stdin, stdout, stderr = client.exec_command(cmd)
        for std in stdout.readlines():
            print(std)
    else:
        stat += 1
        time.sleep(1)
        if stat == 5:
            break
