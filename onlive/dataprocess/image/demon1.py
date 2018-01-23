#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 21:50
# @Author  : lingxiangxiang
# @File    : demon1.py

from PIL import Image

image = Image.open("1.jpg")
print(image.format, image.size, image.mode)
image.show()