# -*- coding=utf-8 -*-
from tqdm import tqdm

from project.scrawler_tieba.downloader import HtmlDownloader
from project.scrawler_tieba.output import Output
from project.scrawler_tieba.parser import Parser

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
        print("")
        print("what the most hot theme is " + max_object.title
              + " and " + str(max_l) + " people take part in , let's access it ")
        # TODO 直接调用chrome访问地址

        # output data to a container
        # output to html
        # file_name = 'post_statistic_infos.html'
        # self.output.save_to_html_excel(file_name, [max_object])
        # self.output.save_to_text(file_name, [max_object])
        ## output to db(mongodb)


if __name__ == '__main__':

    print('')
    title = 'We are scrawling web is ZZU post website, please enter the end page:'
    url = 'http://tieba.baidu.com/f?kw=%E9%83%91%E5%B7%9E%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
    crawler = Crawler()
    end_page = int(input(title))
    crawler.crawl(url, end_page)
