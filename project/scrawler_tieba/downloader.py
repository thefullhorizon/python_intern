# -*- coding=utf-8 -*-
import socket
import ssl
import urllib.request
import urllib3


class HtmlDownloader(object):

    def download(self, url):

        if url is None:
            print('Address can not be null')
            return
        print("start to download ...")
        # Add cookie
        user_agent = "User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
        headers = {'User-Agent': user_agent}

        # request = urllib.request.Request(url, headers=headers)
        request = urllib.request.Request(url)

        # python 新特性，当使用urllib打开https的链接时，会检验一次ssl证书
        context = ssl._create_unverified_context()
        try:
            response = urllib.request.urlopen(request, context=context, timeout=5)
            if response.getcode() != 200:
                return None
            print("end to download ...")
            return response.read()
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                print("Time out!")

    def download_new(self, url):
        if url is None:
            print('Address can not be null')
            return
        print("start to download ...")
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        if response.status != 200:
            return None
        print("end to download ...")
        return response.read()
