# -*- coding: utf-8 -*-
import time

from bs4 import BeautifulSoup
from datetime import datetime
from project.scrawler_tieba.downloader import HtmlDownloader

"""
该模块主要自动化获取一些自己感兴趣的数据
"""


def show_diff_time():
    """
    获得距离年初已经几天了
    :return:
    """
    current_day = datetime.now()
    diff01 = current_day - datetime(2020, 1, 1)
    diff02 = datetime(2021, 1, 1) - current_day
    print("今天是第{}天,距离2021年还有{}天".format(diff01.days+1, diff02.days-1))


def show_pm25():
    """
    从关注的数据源中获取可靠的PM2.5数据
    :return:
    """
    html_loader = HtmlDownloader()
    html_url = 'http://aqicn.org/city/shanghai/cn/'
    html_doc = html_loader.download(html_url)
    bsoup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

    print('------------------- LS COMPREHENSIVE DATA CENTER -------------------')
    result = bsoup.find_all('div', class_='aqivalue', id='aqiwgtvalue')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("PM2.5 Info : " + result[0].get_text())
    print("Suggestion : " + result[0].get('title'))


if __name__ == "__main__":
    show_diff_time()
