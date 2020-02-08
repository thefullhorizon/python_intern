# -*- coding: utf-8 -*-
import re

from bs4 import BeautifulSoup
from scrawler_demos.tieba.post_statistic_info import PostStatisticInfo


class Parser(object):


    def get_last_number(self, html_doc):
        """
        # href = "//tieba.baidu.com/f?kw=%E9%83%91%E5%B7%9E%E5%A4%A7%E5%AD%A6&amp;ie=utf-8&amp;pn=810950"
        :param html_doc:
        :return: 810950
        """
        bsoup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
        last_url = bsoup.find('a', class_='last pagination-item ')['href']
        return int(last_url.split('pn=')[1])

    def parser_zhengda_tieba(self, html_url, html_doc):
        """
        obtain statistic of viewing of each post base on specified html content
        :return: list
        """
        print("start to parse ")
        bsoup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

        post_statistic_infos = []
        base_url = 'http://tieba.baidu.com'
        div_nodes = bsoup.find_all('div', class_='t_con cleafix')

        for div_node in div_nodes:
            item = PostStatisticInfo()

            node_number = div_node.find('span', class_='threadlist_rep_num center_text')
            item.number = int(node_number.string)

            node_right = div_node.find('a', href=re.compile(r'/p/[0-9]+'))

            item.title = node_right['title'].encode('utf-8')
            item.url = base_url + node_right['href'].encode('utf-8')

            # 添加进mongoDB
            # item.save_to_db()
            # 添加进内存
            post_statistic_infos.append(item)

        print("complete to parse ")
        return post_statistic_infos
