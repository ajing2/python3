#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 23:53
# @Author  : lingxiangxiang
# @File    : demon.py


a = input("please input a number:")
try:
    result = 100/int(a)
except Exception as e:
    print("除数不能为0！")
    raise e
else:
    print("恭喜你完成了除的操作， result = {0}".format(result))
finally:
    print("不管有没有异常，都必须干的事情！")


try:
    f = open("__init__.py")
    print(f.read())
except Exception as e :
    raise e
finally:
    f.close()
