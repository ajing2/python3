#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 21:59
# @Author  : lingxiangxiang
# @File    : demon8.py

from PIL import Image
image = Image.open("1.jpg")
print(image.format, image.size, image.mode)
box = (600, 300, 1050, 660)
region = image.crop(box)
region.save("cutting.jpg")
# region.show()
# 上述代码讲图片的((600, 300), (600, 660), (1050, 300), (1050, 660))所画出来的区域进行裁剪，并保存在cutting.jpg中
region1 = region.transpose(Image.ROTATE_180)
image.paste(region1, box)
image.show()
