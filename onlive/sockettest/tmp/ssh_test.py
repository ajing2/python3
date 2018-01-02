#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 11:02
# @Author  : lingxiangxiang
# @File    : ssh_test.py
import paramiko
# pkey='E:/wamp/www/tools/id_rsa'  #本地密钥文件路径[此文件服务器上~/.ssh/id_rsa可下载到本地]
# key=paramiko.RSAKey.from_private_key_file(pkey,password='******') #有解密密码时,
# paramiko.util.log_to_file('paramiko.log')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 允许连接不在know_hosts文件中的主机
client.connect('192.168.48.131', 22, username='root', password='123456', timeout=4)

# ssh.connect('10.120.48.109', port, '用户名',key_filename='私钥')
while 1:
  shell = input("[root@localhost ~]#")
  stdin, stdout, stderr = client.exec_command(shell)
  for std in stdout.readlines():
    print(std)
client.close()