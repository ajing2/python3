#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 16:16
# @Author  : lingxiangxiang
# @File    : demonsysrandom.py

import sys
import random

print(sys.argv[0])
print(sys.argv[1])

# stdin
# stdout
# stderr
#
# f = open("1.log", "w")
# sys.stdout = f
# print("hello world")

print(random.random())
print(random.randint(10, 20))
print(random.uniform(10, 20))
print(random.randrange(10, 100, 2))
print(random.sample("asdlkfjalsdjmlkaujf", 4))


import string
print(string.ascii_letters)
print(string.hexdigits)
print(string.digits)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.printable)

strs = string.ascii_letters + string.digits
print(strs)
l = str()
for i in random.sample(strs, 4):
    l += i
print(l)
