# -*- coding=utf-8 -*-
"""

将于文件相关的操作统一在这里进行封装

Author       :   Cucumber
Date         :   10/21/20

"""

import json


def save_dict(file, dict_obj):
    """
    将字典数据保存在文件中
    :param file:
    :param dict_obj:
    """
    js = json.dumps(dict_obj)
    file = open(file, 'w')
    file.write(js)
    file.close()


def read_dict(file):
    """
    :param file:
    :return: 从文件中读取字典数据
    """
    file = open(file, 'r')
    js = file.read()
    dict_obj = json.loads(js)
    file.close()
    return dict_obj

