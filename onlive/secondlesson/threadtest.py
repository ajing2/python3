#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 20:48
# @Author  : lingxiangxiang
# @File    : threadtest.py
import codecs
from queue import Queue
from threading import Thread

import time


class Produce(Thread):
    def __init__(self, queue):
        super(Produce, self).__init__()
        self.fileName = "../firstlession/passwd"
        self.fileList = list()
        self.queue = queue
    def run(self):
        with codecs.open(self.fileName) as f:
            self.fileList += f.readlines()
        for line in self.fileList:
            self.queue.put(line)

class Consumer(Thread):
    def __init__(self, queue):
        self.queue = queue
        super(Consumer, self).__init__()
        self.newPasswd = "newpasswd.txt"
        self.fileList = list()
        self.stat = 1
    def run(self):
        while 1:
            if self.queue.empty():
                time.sleep(2)
                self.stat += 1
                if self.stat == 5:
                    break
            else:
                self.stat = 1
                data = self.queue.get()
                self.fileList.append(data)

        with codecs.open(self.newPasswd, 'w') as f:
            f.writelines(self.fileList)


