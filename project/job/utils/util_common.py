# -*- coding=utf-8 -*-

# driver必须为全局变量，否则会出现浏览器打开闪退
import time
from selenium import webdriver


def open_url(path):
    """
    打开指定的网页
    :param path:
    """
    if path.find("file") <= 0:
        path += "file://"
    # 这句话使用的时候要放在全局（方法外部），否则会引起浏览器页面闪退
    # driver = webdriver.Chrome()
    # driver.get(path)


def get_current_date():
    """
    :return: 获取当前日期
    """
    return time.strftime("%Y%m%d", time.localtime())
