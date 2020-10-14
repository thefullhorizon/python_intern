# -*- coding=utf-8 -*-

# driver必须为全局变量，否则会出现浏览器打开闪退
from selenium import webdriver

driver = webdriver.Chrome()


def open_url(path):
    # 直接使用网页打开
    if path.find("file") <= 0:
        path += "file://"
    driver.get(path)
