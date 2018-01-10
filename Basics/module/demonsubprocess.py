#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 14:18
# @Author  : lingxiangxiang
# @File    : demonsubprocess.py

import subprocess

status, result = subprocess.getstatusoutput("ipconfig")

try:
    if status == 0:
        print(result)
except Exception as e:
    raise e