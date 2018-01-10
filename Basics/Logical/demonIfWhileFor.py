#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 16:07
# @Author  : lingxiangxiang
# @File    : demonIfWhileFor.py


# python缩进
# main:
#     print("hello")
# print("hello world")
# c  main(param){}
# java  main(param){}

# if 判断条件：
#     执行语句
# elif 判断条件：
#     执行语句
# else：
#     执行语句


# while 判断条件：
#     执行语句
a = 100
while a>1:
    print(a)
    a -=1
    if a == 50:
        break#退出循环
    if a == 55:
        print("555555555555555")
        continue


# break    跳出循环
# continue    进入下一次循环



# for item in sequence:
#     执行语句

l = ['a', 'b', 'c', 'd', 'e']
print(l[0:5])#  大于等于0   小于5   0<=a<5
print(l[0:-1])#  大于等于0   小于5   0<=a<5
print(l[:])#  大于等于0   小于5   0<=a<5
for x, y in enumerate(l):
    print(x, y)
