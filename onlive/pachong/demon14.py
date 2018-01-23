#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 22:15
# @Author  : lingxiangxiang
# @File    : demon14.py
import random
import time

import os
from selenium import webdriver


def random_sleep(min, max):
    time.sleep((max-min) * random.random() + min)


url = "https://passport.jd.com/new/login.aspx"

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url=url)

driver.find_element_by_xpath('//a[@clstag="pageclick|keycount|201607144|2"]').click()
# time.sleep(30)
random_sleep(1, 5)
driver.find_element_by_id("loginname").send_keys("xxxxxxxx")
random_sleep(1, 4)
driver.find_element_by_id("nloginpwd").send_keys("xxxxxxxx")
random_sleep(2, 3)
driver.find_element_by_id("loginsubmit").click()
print(driver.get_cookies())
time.sleep(30)
driver.quit()
