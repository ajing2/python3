#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 15:51
# @Author  : lingxiangxiang
# @File    : demonMethod.py

# help()  ctrl + 鼠标左键
s = "sadfasdfas"
help(s.split)
restult = s.startswith("sa")
print(restult)

# dir()
print(dir(s))

# type()
a = '123'
print(type(a))
print(type(int(a)))


# len(s)   统计字符串的长度
print(len(s))


# isinstance(a, type)   返回值是一个bool类型

print(isinstance(s, str))
print(isinstance(s, dict))



# python 2  print支持  print s1,s2, s3   就是不回车
# python 3   print 包装一个函数，print(s, end="")   这个是不回车

# python 2中存在     xrange() range()     d.iteritems()  d.items()
# python 3 中只存在   range()   itemws()


# python2    input   输入的必须是整数， raw_input 自动把输入的改成字符类型
# python3    input   注入的自动都转换成字符串类型
