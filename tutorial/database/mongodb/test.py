# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime
import json

from tutorial.database.mongodb.api import *
from tutorial.database.mongodb.initial_data import post
from tutorial.database.mongodb.initial_data import posts

# 解决TypeError: datetime.datetime(2017, 10, 23, 3, 47, 15, 491000) is not JSON serializable


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# query_all()
# update()
# delete()
query_all()

