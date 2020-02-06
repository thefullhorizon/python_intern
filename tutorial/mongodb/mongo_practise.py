# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime
import json

from tutorial.mongodb.mongo_encap import MongoUtil


# 解决TypeError: datetime.datetime(2017, 10, 23, 3, 47, 15, 491000) is not JSON serializable
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


mongo_util = MongoUtil()
db_zzu = mongo_util.get_db('zzu')
# 查询数据库中所有的collections
# print db_zzu.collection_names()

# create collection post
collection_post = db_zzu['post']

post = { 'author': 'horizon',
'content': 'a programmer',
'date': datetime.now()}

posts = [{
'author': 'horizon',
 'content': 'a programer',
 'date': datetime.now()
}, {
'author': 'sharp',
 'content': 'a teacher',
 'date': datetime.now()
}, {
'author': 'ocean',
 'content': 'a driver',
 'date': datetime.now()
}
]

# 重新生成的数据
# collection_post.remove()
# collection_post.insert_many(posts)
print(collection_post.find().count())
selected_item = None
for item in collection_post.find():
    if selected_item is None:
        selected_item = item
        continue
    if item['number'] > selected_item['number']:
        selected_item = item

print('%s(%d) : %s' % (selected_item['title'],  selected_item['number'], selected_item['url']))





# dict 与json的互转
# str_data = json.dumps(post, cls=CJsonEncoder)
# print type(str_data)
#
# dict_data = json.loads(str_data)
# print dict_data['author']
