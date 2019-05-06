# 第一个Python程序

'''
userName = input()
print('Hello',userName)
'''

############################## Python 基础 ##############################

#字符串和编码

'''
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
'''

#使用list和tuple
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
#条件判断
'''
if 3>2:
    print('It is correct')
'''
#循环
'''
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

print(list(range(10)))
'''
#使用dict和set

############################## 函数 ##############################
'''
def person(name, age,**kw):
    print('name:',name,'age:',age,'other:',kw)

extra = {'city':'beijing','job':'Engineer'}
#person('jack',24,city = extra['city'],job = extra['job'])
person('jack',24,**extra)
'''
############################## 高级特性 ##############################
'''
L = ['NASHAN','HORIZON',"JINGZHOU"]
print(L[-2:])

'''
#['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#Generator
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

############################## 面向对象高级编程 ##############################
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