# -*- coding:utf-8 -*-

class Student(object):
    pass

print("给实例添加属性：")
s = Student()
s.name='zhang'
print(s.name)

print('给实例添加方法：')
def setAge(self, age):
    self.age = age
from types import MethodType
s.setAge = MethodType(setAge, s) #给实例绑定一个方法
s.setAge(50) #调用绑定的方法
print(s.age)

print('给一个实例绑定的方法，对另一个实例是不起作用的，所以我们需要给类绑定方法：')