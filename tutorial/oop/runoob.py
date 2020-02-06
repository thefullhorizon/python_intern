
##################################### OOP

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def withName(self):
        return self.name

    def prt(self):
        print(self)
        print(self.__class__)
        print(__dict__)
        print(__name__)
        # print(self.__dict__)


# s = Student('horizon',18)
# s.prt()

print(Student.__name__)
print(Student.__dict__)
print(Student.__main__)

