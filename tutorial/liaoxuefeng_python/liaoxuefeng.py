import sys
import functools
from PIL import Image
#####################################
'''
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('before call %s:' % func.__name__)
        func(*args, **kw)
        print('after call %s:' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def horizon():
    print('wahaha')

im = Image.open('D:\Pics_2017\cloud.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,160))
im.save('D:\Pics_2017\horizon.jpg','JPEG')
'''

##################################### OOP
'''
class Student(object):
    def __init__(self,name,score):
        self.__name = name;
        self.__score = score;
    def get_score(self):
        print('%s' % self.__score )
horizon = Student('nanshan',99)
haiya = Student('haiya',39)
#horizon.get_score()
#haiya.get_score()
horizon.__score = 0#这句话实际上给实例对象增加了一个新的变量而是，Class内部的属性默认别解释器变成了_Student__name
print(horizon._Student__score)
print(haiya.__score)
'''

##################################### OOP advanced
'''
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda name: Chain('%s/users/%s'%(self._path,name))
        else:
            return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().site.users('horizon').gsd)
'''
import logging
logging.basicConfig(level=logging.INFO)
from enum import Enum, unique
'''
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
'''
'''
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# for name, member in Weekday.__members__.items():
#     print(name, '=>', member, ',', member.value)
print(logging.info('horiozn'))

'''

##################################### IO programming
# write

# f = open('E:\Pycharm\horizon.txt','wb')
# f.write('南山'.encode('utf-8'))
# f.write('\n')
# f.write('jing')

# read

# f = open('E:\Pycharm\horizon.txt','rb')
# for line in f.readlines():
#     print(line.decode('utf-8'))

# f.close()

import os

# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# print(__name__)
# print(os.getpid())
# print(os.fork())

##################################### 进程and线程

import threading, multiprocessing
# 输出CPU核数
# print(multiprocessing.cpu_count())

import re
'''
test1 = 'someone@163.com'
re_email1 = r'([0-9a-zA-Z]+?)\@([0-9a-z]+)'
print(re.match(re_email1, test1).groups()[0])

test2 = 'someone@163.com'
re_email2 = r'[a-z]+\@[0-9]+\.com'
if re.match(re_email2, test2):
    print('TRUE')
else:
    print("FALSE")
'''

##################################### 常用第三方模块
'''
from PIL import Image, ImageFilter

im = Image.open('D:\Pics_2017\grass.jpg')
print(im.size)
im2 = im.filter(ImageFilter.BLUR)
im2.save('D:\Pics_2017\grass01.jpg','jpeg')
'''
##################################### 图形界面
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()