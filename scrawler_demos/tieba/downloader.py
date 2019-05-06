# -*- coding=utf-8 -*-
import urllib2
# python3x
# import urllib.request
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            print 'Address can not be null'
            return
        print "start to download "
        # Add cookie
        user_agent = "User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
        headers = {'User-Agent':user_agent}
        request = urllib2.Request(url, headers=headers)

        try:
            response = urllib2.urlopen(request, timeout=10)
        except urllib2.HTTPError, e:
            print e.code
        except urllib2.URLError, e:
            print e.reason

        if response.getcode() != 200:
            return None
        print "end to download "
        return response.read()
