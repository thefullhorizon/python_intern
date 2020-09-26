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
        # Add cookie
        user_agent = "User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
        headers = {'User-Agent': user_agent}

        request = urllib.request.Request(url, headers=headers)

        # python 新特性，当使用urllib打开https的链接时，会检验一次ssl证书
        context = ssl._create_unverified_context()
        try:
            response = urllib.request.urlopen(request, context=context, timeout=5)
            if response.getcode() != 200:
                return None
            return response.read()
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                print("Time out!")
