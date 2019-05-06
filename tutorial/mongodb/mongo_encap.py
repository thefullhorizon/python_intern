# -*- coding: utf-8 -*-
from pymongo import MongoClient


class MongoUtil(object):

    def get_db(self, db_name):
        '''

        :param db_name: db name
        :return:
        '''
        client = MongoClient('mongodb://localhost:27017/')
        return client[db_name]
