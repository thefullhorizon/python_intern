# -*- coding: utf-8 -*-


class Animal(object):
    pass


class Student(object):

    def __init__(self, name=None, score=-1):
        self.name = name
        self.score = score

    def print_info(self):
        print('%s : %d' % (self.name, self.score))

if __name__ == '__main__':

    # experiment how to use class
    student = Student(score=90)
    student.print_info()

    # experiment str split


