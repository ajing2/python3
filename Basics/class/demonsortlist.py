#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 22:04
# @Author  : lingxiangxiang
# @File    : demonsortlist.py

class GetList(object):
    def __init__(self):
        self.data = self.get_data()
        self.intList = self.listStrToInt(self.data)

    def get_data(self):
        data = input("please input a string(like: 23,45,65,7,68,88……):")
        result = self.isok(data)
        if result:
            return data
        else:
            print("the data of your input is error.")
            exit(1)
    def isok(self, data):
        oklist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ',']
        result = True
        for i in data:
            if i not in oklist:
                result = False
                break
        return  result
    def listStrToInt(self, data):
        l = list()
        for i in data.split(","):
            l.append(int(i.strip()))
        return l






class BubbleSort(GetList):
    def __init__(self):
        super(BubbleSort, self).__init__()
        print(self.sortList(self.intList))
    def sortList(self, list):
        for i in range(0, len(list)):
            for j in range(i+1, len(list)):
                if list[i] > list[j]:
                    a= list[i]
                    list[i] = list[j]
                    list[j] = a
        return list


if __name__ == '__main__':
    bubbleSort = BubbleSort()