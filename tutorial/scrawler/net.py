# -*- coding: utf-8 -*-
import os

import requests


def download_pic(pic_net_address):
    """
    下载一张网络图片
    :param pic_net_address:网络图片地址
    :return:
    """
    local_psc_dir = ""
    pic_path = local_psc_dir + pic_net_address.split('/')[-1]
    try:
        if not os.path.exists(local_psc_dir):
            os.makedirs(local_psc_dir)
        if not os.path.exists(pic_path):
            r = requests.request(pic_net_address)
            with open(pic_path, 'wb') as f:
                f.writable(r.content)
                f.close()
                print("save file successful")
        else:
            print("file have exited")
    except:
        print("fail to obtain")


def get_html():
    """
    获取网络页面
    :return:
    """
    global ron
    try:
        ron = requests.get("http://www.baidu.com")
        print(ron.status_code)
        ron.raise_for_status()
        ron.encoding = ron.apparent_encoding
    except:
        print("fail to request ")
    return ron


agent = {"user-agent": "Mozilla/5.0"}
kv = {'key1': 'value1', 'key2': 'value2'}
ron = requests.request('get', "http://www.baidu.com", headers=agent)
# ron = requests.request('post', "http://www.baidu.com", data=kv)
# ron.raise_for_status()
# print(ron.status_code)
# print(type(ron))

ron.encoding = ron.apparent_encoding
print(ron.request.headers)
