# -*- coding=utf-8 -*-
from project.scrawler_tieba.downloader import HtmlDownloader

from project.scrawler_tieba.output import Output
from project.scrawler_tieba.parser import Parser
from tqdm import tqdm


class Crawler(object):

    def __init__(self):
        # initialize tools
        self.loader = HtmlDownloader()
        self.parser = Parser()
        self.output = Output()

    def crawl(self, url, end_page):

        """
        define the scrawled page
        :param url:
        :param end_page: -1 表示用户没指定页数，则爬取得全部帖子
        :return:
        """
        post_statistic_infos = []
        # if end_page == -1:
        #     end_page = parser.get_last_number() + 1
        print("")
        print(">>> Data obtain...")
        for i in tqdm(range(end_page)):
            # generate valid url
            pn = 50 * i
            complete_url = url + str(pn)

            # download into local
            html_doc = self.loader.download(complete_url)
            if html_doc is None:
                print('Net work exception')
                return
            # parse data
            result = self.parser.parser_zhengda_tieba(html_doc)
            for item in result:
                # 数据存入list中
                post_statistic_infos.append(item)

        # analysis the data
        print("")
        print(">>> Data analysis...")
        max_l = 0
        max_object = None
        for item in post_statistic_infos:
            if max_l < item.number:
                max_l = item.number
                max_object = item

        return max_object
