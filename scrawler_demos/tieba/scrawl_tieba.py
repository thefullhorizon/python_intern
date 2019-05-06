# -*- coding=utf-8 -*-

from scrawler_demos.tieba.downloader import HtmlDownloader
from scrawler_demos.tieba.output import Output
from scrawler_demos.tieba.parser import Parser

'''

powered by horizon

what implement mian functions:
    1. crawl ZZU post : my first crawler project in a special sense from 2017-10-16 to 2017-10-19 costing 4 days

Archive at : /Youdao/COM/Python/Web crawler
'''


class Crawler(object):

    def __init__(self):
        # initialize tools
        self.loader = HtmlDownloader()
        self.parser = Parser()
        self.output = Output()

    def crawl(self, url, end_page):

        '''
        define the scrawled page
        :param url:
        :param end_page: -1 表示用户没指定页数，则爬取得全部帖子
        :return:
        '''
        post_statistic_infos = []
        # if end_page == -1:
        #     end_page = parser.get_last_number() + 1
        for i in range(1, end_page + 1):

            # generate valid url
            pn = 50 * (i - 1)
            complete_url = url + str(pn)
            print ">>> crawling all web pages"
            print "start to crawl page number " + str(i) + " : "+complete_url

            # download into local
            html_doc = self.loader.download(complete_url)

            # parse data
            result = self.parser.parser_zhengda_tieba(complete_url, html_doc)
            for item in result:
                # 数据存入list中
                post_statistic_infos.append(item)

        print ">>> crawled all web pages"

        # analysis the data
        print ">>> start to analysis"
        max_l = 0
        for item in post_statistic_infos:
            if max_l < item.number:
                max_l = item.number
        print ">>> end to analysis "
        # print "what the result is : " + max_l
        # output data to a container

        # output to html
        file_name = 'post_statistic_infos.html'
        self.output.save_to_html(file_name, post_statistic_infos)

        ## output to db(mongodb)


if __name__ == '__main__':

    print 'we are scrawling web is ZZU post website ...'
    url = 'http://tieba.baidu.com/f?kw=%E9%83%91%E5%B7%9E%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
    crawler = Crawler()
    end_page = int(raw_input('enter the end page: '))
    crawler.crawl(url, end_page)
    # crawler.crawl(url, 10)
