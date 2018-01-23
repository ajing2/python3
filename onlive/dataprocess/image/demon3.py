#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 22:08
# @Author  : lingxiangxiang
# @File    : demon9.py
from PIL import Image

infile = "1.jpg"
outfile = "new2.jpg"
image = Image.open(infile)
(x, y) = image.size
newx = 300
newy = int(y*newx/x)
out = image.resize((newx, newy), Image.ANTIALIAS)
# out.show()
out.save(outfile)
