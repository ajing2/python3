#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 22:13
# @Author  : lingxiangxiang
# @File    : demon11.py
import urllib.request
import http.cookiejar

url = "http://www.hao123.com"
cookieFile = "cookie.txt"

cookiehao = http.cookiejar.MozillaCookieJar(cookieFile)
cookiehao.load(cookieFile)
print(cookiehao)

req = urllib.request.Request(url)
handler = urllib.request.HTTPCookieProcessor(cookiehao)
opener = urllib.request.build_opener(handler)
res = opener.open(req)
