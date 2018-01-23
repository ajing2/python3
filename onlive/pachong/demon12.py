#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 20:53
# @Author  : lingxiangxiang
# @File    : demon12.py
import os

import time
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")
element.clear()
element.send_keys("你好")
elementsubmit = driver.find_element_by_id("su")
elementsubmit.click()


time.sleep(30)

print(driver.get_cookies())
driver.quit()




