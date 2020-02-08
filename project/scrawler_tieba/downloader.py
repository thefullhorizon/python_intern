# -*- coding=utf-8 -*-
import socket
import urllib.request
# python3x
# import urllib.request

# unique download tools


class HtmlDownloader(object):

    @staticmethod
    def download(url):

        if url is None:
            print('Address can not be null')
            return
        print("start to download ...")
        # Add cookie
        user_agent = "User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
        headers = {'User-Agent': user_agent}
        request = urllib.request.Request(url, headers=headers)
        global response
        try:
            response = urllib.request.urlopen(request, timeout=5)
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                print("Time out!")

        if response.getcode() != 200:
            return None
        print("end to download ...")
        return response.read()
