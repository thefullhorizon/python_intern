# -*- coding: utf-8 -*-

__author__ = 'horizon'


import re
import urllib
import urllib.request


print('----------------------base API----------------------------')


def module_written():
    """
    紧接着方法下一行来写，可以作为python的文档来看
    :return:
    """
    return 0


print('---------------------- proxy ----------------------------')

url = 'https://pic2.zhimg.com/v2-0ff8d18e29c55d412bbaf52b56ba024d_r.jpg'
response = urllib.request.urlopen(url, timeout=10)
with open("spider.jpg", "wb") as file_img:
    file_img.write(response.read())

'''
print '----------------------re----------------------------'
pattern = re.compile(r'hello')
matchResult = re.match(pattern, 'x hello horizon hello')
if matchResult:
    print matchResult.group(0)
    print matchResult.string
    print matchResult.lastgroup

print '----------------------urllib2 and cookie----------------------------'
# cookielib.CookieJar() 生成cookie变量
filename = 'myCookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
cookie.save(ignore_discard=True, ignore_expires=True)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

request = urllib2.Request('http://python.jobbole.com/all-posts/')
try:
    # response = urllib2.urlopen(request) urlopen()是使用了默认的opener,默认的opener不能处理cookie相关的信息
    response = opener.open(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
print response.read()

for item in cookie:
    print 'Key = ' + item.name
    print 'Value = ' + item.value


# read cookie from file
cookie = cookielib.MozillaCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)
response = opener.open(request)
print response.read()

'''