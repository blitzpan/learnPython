# -*- coding:utf-8 -*-
#定义Person类
class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
#定义Student类继承Person类
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score

s1 = Student('zhangsan','M',90)
print s1,s1.name,s1.gender,s1.score