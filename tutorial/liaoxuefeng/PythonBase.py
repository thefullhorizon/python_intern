# ############################# Python 基础 - 基本概念 ##############################

' this is a doc instruction '
import sys

print(sys.path)

'''
模块：一个.py文件就是一个模块。是一组python代码的集合
包：为了避免模块间存在冲突，一如一个包
每一个包下面默认会创建一个__init__.py模块，标识当前目录是一个包而不是普通目录。
'''


# ############################# Python 基础 - 数据类型 ##############################

'''
基本型：整数，浮点数，字符串，布尔值，空值，变量，常量
对象型：List,tuple,dict,set

'''

# 字符串和编码
'''
第一个Python程序
userName = input()
print('Hello',userName)

print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
'''

# 使用list和tuple
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])#获取导数第1个元素值
classmates.append('Adam')
classmates.insert(1, 'Jack')
classmates.pop()#删除list末尾的元素
classmates.pop(1)#删除list指定位置的元素
'''

# ############################# 函数 ##############################
'''
def person(name, age,**kw):
    print('name:',name,'age:',age,'other:',kw)

extra = {'city':'beijing','job':'Engineer'}
#person('jack',24,city = extra['city'],job = extra['job'])
person('jack',24,**extra)
'''
'''
位置参数：def power(x):
默认参数：def power(x, n=2): 默认参数不需使用不可变参数，推荐使用None
可变参数：def calc(*numbers): 实质是函数内封装成了tuple
关键字参数：def person(name, age, **kw): 
命名关键字参数：def person(name, age, *, city, job): 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

参数定义的顺序必须是：位置参数、默认参数、可变参数、命名关键字参数和关键字参数。

'''


# define a function
# def run(ride_style, road_style="road", *people):
#     print("user use " + ride_style + " on " + road_style + " with " + people)
#     pass
def run(water="2", *args, city, **people):
    print(water)
    print("water", water, args, " in city ", city, " gender is ", people)
    # for (key, value) in people:
    #     print("users are " + key + " value " + value)
    pass


run("heihei", "haha", city="shang hai", gender="male", style="road")

# ############################# 高级特性 ##############################
'''
L = ['NASHAN','HORIZON',"JINGZHOU"]
print(L[-2:])

'''
# ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# Generator
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        a, b = b, a + b
        print(a,b)
        n = n + 1
    return 'done'
fib(6)
'''

# ############################# 面向对象高级编程 ##############################
'''
class A(object):

    __slots__ = ('_name','age')

    def __AK(self):
        pass

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

# print(dir(A))
s = Student()
s.birth = 12
print(s.birth)
'''
