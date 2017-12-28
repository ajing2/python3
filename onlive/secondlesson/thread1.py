#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 21:26
# @Author  : lingxiangxiang
# @File    : thread1.py
from queue import Queue

from onlive.secondlesson.threadtest import Produce, Consumer


def main():
    q = Queue()
    produce = Produce(q)
    consumer = Consumer(q)
    produce.start()
    consumer.start()

if __name__ == '__main__':
    main()