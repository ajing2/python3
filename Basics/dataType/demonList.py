#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 13:08
# @Author  : lingxiangxiang
# @File    : demonList.py


l = [1, 2, 3.141592653, 'a', 'b', 'c', {"name": "lingxiangxiang"}]
print(l)

# append  追加一个元素
l.append('hello')
print(l)

# pop   删除元素， 默认删除最后一个

m = l.pop(2)
print("m = {0}".format(m))
print(l)

# remove  删除元素  remove(value)

l.remove("c")
print(l)

#
# # index(value)   返回value所对应的下标
print(l.index("a"))


# sort()    排序
# reverse()  反序

m = [1,34, 345, 654, 76, 34, 34, 654, 7,34]
print(m)
m.sort()
print(m)
m.reverse()
print(m)

# insert  插入新的元素   insert(index, value)
m.insert(3, "hello")
print(m)



