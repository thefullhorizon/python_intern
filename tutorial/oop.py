# -*- coding: utf-8 -*-

# ------------------------------------Note------------------------------------
'''
1. Class and instance
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

2. 访问限制
在Python中，实例的变量名如果以__（双下划线）开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的
    变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

3. 多态和继承



'''

# ------------------------------------Practise------------------------------------


class Student(object):


    class_var = 'I am a class variable'

    def __init__(self,id,name):
        self.instance_var = 'I am a instance variable'
        self.id = id
        self.name = name

    def printSelf(self):
        print(self.__class__)
        print(self.__module__)

    def instance_method(self, formal_parameter):
        loca_var_in_function = formal_parameter
        self.local_var_also_in_function = formal_parameter

    def ordinary_function(formal_parameter):
        print 'I am an ordinary function, I can not visit class var and instance var'
        # print self.instance_var
        # print class_var

    @classmethod
    def class_method(cls, formal_parameter):
        print 'I am class method, I can visit(modifying) class var and instance var'

        cls.instance_var = formal_parameter
        print 'instance_var : ' + cls.instance_var

        class_var = formal_parameter
        print 'class_var : ' + class_var

    @staticmethod
    def static_method(formal_parameter):
        print 'I am static method, I am the Adopted son(干儿子) for this class!!'
        print "I can't modify anything in the class "
        # print class_var
        # print self.instance_var



ins = Student(32,'horizon')
# 格式化输出
# print('%s : %s ' % (ins.name, ins.id))
# ins.printSelf()

# ins.class_method('new parameter')
ins.static_method('new parameter')







