# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from project.scrawler_demos.tieba.downloader import HtmlDownloader

# 文档参考中心：https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#

# 要解析的本地Html页面
# html = 'index.html'
# 用BS来加载解析
# bsoup = BeautifulSoup(open(html), 'html5lib')

# 要解析的网络页面
html_url = 'http://tieba.baidu.com/f?kw=%E9%83%91%E5%B7%9E%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=0'
html_loader = HtmlDownloader()
# 将文档下载到内存
html_doc = html_loader.download(html_url)
# 使用BS4解析
bsoup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print('------------------- Implementing -------------------')
# last_url = bsoup.find('a', class_='last pagination-item ')['href']
# print last_url.split('pn=')[1]


'''
print '------------------- BS4 main functions -------------------'

# 打印文件体
# print bsoup.prettify()
# print bsoup.title
# print bsoup.head

print '------------------- BS4中的四大对象类型 -------------------'
print type(bsoup.a)
print type(bsoup.title.string)
# Comment 对象是一个特殊类型的 NavigableString 对象
if type(bsoup.a.string) == bs4.element.Comment:
    print bsoup.a.string
    print type(bsoup.a.string)
# 取节点的属性
print bsoup.a['href']

print '---------直接（直接下一级）子节点---------'
print bsoup.head.contents
for child in bsoup.head.children:
    print child

print '---------descendants 所有子孙节点---------'
# for child in bsoup.descendants:
#     print child

print bsoup.head.string
print bsoup.title.string
# 打印xml中所有显示的内容
# for string in bsoup.stripped_strings:
#     print repr(string)

print '---------父节点，全部父节点.parent .parents---------'
# 这里的父是相对于内容（.string）而言的
content = bsoup.head.title.string
for parent in content.parents:
    if parent.name == 'head':
        print parent.name

print '---------兄弟节点，全部兄弟节点.next_sibling .next_siblings .previous_sibling .previous_siblings---------'
print bsoup.a.next_sibling
for sibling in bsoup.a.next_siblings:
    print repr(sibling)

print '---------前后节点，所有前后节点.---------'
print bsoup.head.next_element


print '---------搜索文档树---------'
print bsoup.find_all('a')[0]
print bsoup.find_all(id='link2')
print bsoup.find_all('a', class_='sister',limit=2)

'''


