#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 0:31
# @Author  : lingxiangxiang
# @File    : demonlogging.py

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt=' %Y/%m/%d %H:%M:%S', filename='myapp.log', filemode='w')
logger = logging.getLogger(__name__)


def hello(name):
    print("hello {0}".format(name))

hello("ajing")
logger.info("excute function hello")
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")


