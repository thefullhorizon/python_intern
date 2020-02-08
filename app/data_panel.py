# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup

from project.scrawler_demos.tieba.downloader import HtmlDownloader

"""
该模块主要自动化获取一些自己感兴趣的数据
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

