# -*- coding: utf-8 -*-
from tutorial.mongodb.mongo_encap import MongoUtil

'this is a document instruction'

__author__ = "horizon"

class PostStatisticInfo(object):

    zzu_collection = None

    def __init__(self, number=0, title=None, url=None):
        self.number = number
        self.title = title
        self.url = url

    def print_info(self):
        print ('%d : %s : %s' % (self.number, self.title, self.url))

    def get_data(self):
        return self.title + " " + str(self.number) + " " + self.url

    def save_to_db(self):
        # 初始化数据库
        if PostStatisticInfo.zzu_collection is None:
            mongo_util = MongoUtil()
            zzu_db = mongo_util.get_db('zzu')
            PostStatisticInfo.zu_collection = zzu_db['post']
        self.zu_collection.insert(dict(number=self.number, title=self.title, url=self.url))
