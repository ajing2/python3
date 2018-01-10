#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 11:27
# @Author  : lingxiangxiang
# @File    : demon2.py
'''this demon is to test'''
# 整型  int
a = 10
print(a)
# print a     python2  支持

# bool   True    False
# >=1   True
# <=0   False

# float  浮点型
a = 3.141592653
m = round(a, 3)
print(m)


# 字符串  str   'abc'     "abc"     '''abc'''
string = "  abcadeafghaiagh   "
print(string)


# find  查找自字符串，如果找到，返回子字符串开始的下标，如果没有找到，返回-1
print(string[0])
result = string.find('def')
print(result)

# replace   替换
print(string.replace('a', "AAA"))



# split()   分隔符
# join(可迭代的对象)   一般是一个list
newList = string.strip().split('a')
print(newList)
print("  ###  ".join(newList))



# strip()  去除字符串前后的空字符
string.strip()


#一定要用format这种格式
print("my string is : %s" %string)
print("my string is : {0}".format(string))

print("hello " + "wolrd")
