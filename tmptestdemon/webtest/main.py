#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 13:24
# @Author  : lingxiangxiang
# @File    : main.py
from threading import Thread

import web

from tmptestdemon.webtest.util import WebServer

urls = (
    '/', 'index',
    '/ws', 'websocket',
    '/app/aaa', 'appaaa',
    # '/app/bbb', 'appbbb',
    # '/app/ccc', 'appccc',
    # '/app/aaa', 'appddd',
)
menus = (
            {"name": "应用工具", "menus": [
                {"name":"webssh", "url": "'/app/aaa'"},
                {"name": "bbb", "url": "'/app/bbb'"},
                {"name": "ccc", "url": "'/app/ccc'"}
            ]},
            {"name": "数据库工具", "menus": [
                {"name": "ddd", "url": "'/db/ddd'"},
                {"name": "eee", "url": "'/db/eee'"},
                {"name": "fff", "url": "'/db/fff'"}
            ]},
            {"name": "其他", "menus": [
                {"name": "ggg", "url": "'/qt/ggg'"},
                {"name": "hhh", "url": "'/qt/hhh'"},
                {"name": "iii", "url": "'/qt/iii'"}
            ]})

class index:
    def GET(self):
        render = web.template.render("templates")
        return render.main(menus, "lingjing")

class appaaa():
    def GET(self):
        render = web.template.render("templates")
        return render.appaaa()

class websocket():
    def GET(self):
        print("hello ")




if __name__ == "__main__":
    app = web.application(urls, globals())
    webServer = WebServer()
    webServer.start()
    app.run()
