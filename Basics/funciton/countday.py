#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 12:01
# @Author  : lingxiangxiang
# @File    : countday.py

runnian = dict()
a = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6":30, "7":31, "8": 31, "9": 30, "10": 31, "11": 30, "12":31}
b = {"1": 31, "2": 29, "3": 31, "4": 30, "5": 31, "6":30, "7":31, "8": 31, "9": 30, "10": 31, "11": 30, "12":31}
runnian["yes"] = b
runnian["no"] = a
print(runnian)


def panduan(year):
    if (year%4==0&year%100!=0)|year%400==0:
        return True
    else:
        return False


def isint(date):
    year, month, day = date.split("-")
    if int(year)<0:
        return False
    if int(month) not in range(1, 13):
        return False
    if panduan(int(year)):
        for i in runnian["yes"].keys():
            if month == i:
                if int(day)>0 and int(day)<=runnian["yes"][i]:
                    return True
                else:
                    return False
    else:
        for i in runnian["no"].keys():
            if month == i:
                if int(day)>0 & int(day)<= runnian["no"][i]:
                    return True
                else:
                    return False




def countdays(date):
    days = 0
    year, month, day = date.split("-")
    if panduan(int(year)):
        # if int(month)<3:
        #     days = 31 + day
        #     print("{0}是今年的第{1}天".format(date, days))
        # else:
        for i in range(1, int(month)):
            days += runnian["yes"][str(i)]
        days += int(day)
        print("{0}是今年的第{1}天".format(date, days))
    else:
        for i in range(1, int(month)):
            days += runnian["no"][str(i)]
        days += int(day)
        print("{0}是今年的第{1}天".format(date, days))



def main():
    date = input("data(like 1970-1-1): ")
    ok = isint(date)
    if ok:
        countdays(date)
    else:
        print("输入有误！")


if __name__ == '__main__':
    main()