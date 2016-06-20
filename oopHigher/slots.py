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
Student.setAge = setAge
s1 = Student()
s1.setAge(10)
print(s1.age)

#
print('我们不想让每个人都能随便的改实例的属性怎么办？添加__slots__，限制动态添加的属性名')
class Student(object):
    __slots__=('name','sex')#限制只能有这些属性
s = Student()
s.name='ZhangSan'
s.sex="男"
#s.age=18 #这里就会报错，Student没有age这个属性。

#
class GraduateStu(Student):
    pass
g = GraduateStu()
g.age = 18 #如果子类没有__slots__，那么父类定义的对子类不起作用
print(g.age)
#
class GraduateStu(Student):
    __slots__=('birth')
    pass
g = GraduateStu()
g.name = 18 #如果子类有__slots__，那么真正的slots是父子类相加。
print(g.name)