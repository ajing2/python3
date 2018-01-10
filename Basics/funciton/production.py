#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 14:09
# @Author  : lingxiangxiang
# @File    : production.py

y = list()
x = [1, 2, 3, 4, 5]
y +=x
y.append(100)
print(y)
print(x)


a = [x*x for x in range(1, 30) if x%2 ==0]
print(a)
print(type(a))

b = (x*x for x in range(1, 30) if x%2 ==0)
print(b)
print(type(b))
for i in b:
    print(i)



def test(l):
    for i in l:
        yield i
        print("i = {0}".format(i))

m = test([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(m))

for i in m:
    print(i)