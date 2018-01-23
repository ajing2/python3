#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 21:51
# @Author  : lingxiangxiang
# @File    : demon10.py

from urllib import request
import http.cookiejar


url = "http://www.hao123.com"
cookieFile = "cookie.txt"
req = request.Request(url)
# cookiejar = cookiejar.CookieJar()
cookiehao = http.cookiejar.MozillaCookieJar(cookieFile)

handler = request.HTTPCookieProcessor(cookiehao)
opener = request.build_opener(handler)
result = opener.open(req)
print(cookiehao)
cookiehao.save()

