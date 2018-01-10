#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 15:06
# @Author  : lingxiangxiang
# @File    : demonDict.py


# 字典的定义：
d1 = dict(name = "ling", age = 25)
d2 = {"id": 10001, "name" : "lingxiangxiang"}
d3 = dict([("ip", "1.1.1.1"), ("address", "beijing")])
print(d1)
print(d2)
print(d3)

# 方法：
# get(key)  根据key获取value
# setdefault 根据key获取value，如果key不存在，可以设定默认的value
print(d1.get("name"))
print(d1.get("address"))
print(d1.setdefault("name"))
print(d1.setdefault("address", "beijing"))

print(d2.keys())
print(type(d2.keys()))
for i in d2.keys():
    print(i)
print(d2.values())

# python 2中 有items  和iteritems

for x, y  in d3.items():
    print("key = {0}, value = {1}".format(x, y))

# update   就跟我们list中的  +相似

m = dict()
n = dict(name = "ling", age = 18)
m.update(n)
print(m)
#
#
# l = list()
# m = [1, 2, 3, 4, 5, 6]
# l += m
# print(l)


print(d3)
# pop(key)    删除key所对应的元素, 返回key所用的value值
keyDelete = d3.pop("ip")
print(keyDelete)
print(d3)
