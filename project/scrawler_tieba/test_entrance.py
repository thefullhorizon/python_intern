# -*- coding=utf-8 -*-
import webbrowser
from selenium import webdriver

from project.scrawler_tieba.crawl import Crawler

'''

powered by horizon

what implement mian functions:
    1. crawl ZZU post : my first crawler project in a special sense from 2017-10-16 to 2017-10-19 costing 4 days

Archive at : /Youdao/COM/Python/Web crawler
'''

if __name__ == '__main__':
    print('')
    title = 'We are scrawling web is ZZU post website, please enter the end page:'
    url = 'http://tieba.baidu.com/f?kw=%E9%83%91%E5%B7%9E%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
    crawler = Crawler()
    end_page = int(input(title))
    the_hot_item = crawler.crawl(url, end_page)

    print("")
    print("what the most hot theme is " + the_hot_item.title
          + " and " + str(the_hot_item.number) + " people take part in , let's access it ")

    # 使用浏览器直接打开
    # 方式一（recommend）
    webbrowser.open(the_hot_item.url)
    # 方式二
    # driver = webdriver.Chrome()
    # driver.get(the_hot_item.url)

    # output data to a container
    # output to html
    # file_name = 'post_statistic_infos.html'
    # self.output.save_to_html_excel(file_name, [the_hot_item])
    # self.output.save_to_text(file_name, [the_hot_item])

    ## output to db(mongodb)
