#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 21:58
# @Author  : lingxiangxiang
# @File    : demon13.py
import random
import time

import os
from selenium import webdriver


def random_sleep(min, max):
    time.sleep((max-min) * random.random() + min)


url = "https://kyfw.12306.cn/otn/login/init"

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url=url)

username = driver.find_element_by_id("username")
username.clear()
random_sleep(1, 5)
username.send_keys("974644081@qq.com")
random_sleep(2, 4)
passwd = driver.find_element_by_id("password")
passwd.send_keys("xxxxxxxx")
time.sleep(5)
random_sleep(1, 3)
submit = driver.find_element_by_id("loginSub")
submit.click()
print(driver.get_cookies())
time.sleep(30)
driver.quit()