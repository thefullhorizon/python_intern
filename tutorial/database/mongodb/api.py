# -*- coding: utf-8 -*-

from pymongo import MongoClient

from tutorial.database.mongodb.initial_data import posts


def get_db(db_name):
    """
    获得指定的数据库连接
    :return:
    """
    client = MongoClient('mongodb://localhost:27017/')
    return client[db_name]


def add():
    """
    添加一条数据
    :return:
    """
    lightning_client = get_db("lightning_storm")
    collections = lightning_client.list_collection_names()
    if 'post' not in collections:
        print("collection post do not exists")
    collection_post = lightning_client['post']
    print("current operate collection: post, and total %s documents" % collection_post.find().count())
    # collection_post.insert(posts)
    collection_post.insert_many(posts)


def delete():
    """
    删除一条数据
    :return:
    """
    lightning_client = get_db("lightning_storm")
    collection_post = lightning_client['post']
    query_one = {"author": "sharp"}
    # query_many = {"name": {"$regex": "^F"}}
    modify = collection_post.delete_one(query_one)
    # modify = collection_post.delete_many(query_many)


def update():
    """
    查找一条数据
    :return:
    """
    lightning_client = get_db("lightning_storm")
    collection_post = lightning_client['post']
    query_one = {"author": "horizon"}
    # query_many = {"name": {"$regex": "^F"}}
    new_values = {"$set": {"author": "sharp"}}
    modify = collection_post.update_one(query_one, new_values)
    # modify = collection_post.update_many(query_many, new_values)
    print("%s document have updated" % modify.modified_count)


def query():
    """
    查询数据
    :return:
    """
    lightning_client = get_db("lightning_storm")
    collection_post = lightning_client['post']
    cols = collection_post.find({"author": "horizon"})
    print("query %s document " % cols.count())
    print_collection(cols)


def query_all():
    """
    查询数据
    :return:
    """
    lightning_client = get_db("lightning_storm")
    collection_post = lightning_client['post']
    print_collection(collection_post.find())


def print_collection(collections):
    """
    打印一个数据集合
    :param collections:
    :return:
    """
    print("Total %s" % collections.count())
    for item in collections:
        print(item)


# dict 与json的互转
# str_data = json.dumps(post, cls=CJsonEncoder)
# print type(str_data)
#
# dict_data = json.loads(str_data)
# print dict_data['author']