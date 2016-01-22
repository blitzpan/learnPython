# -*- coding:utf-8 -*- 
import types
#定义一个方法
def fn_get_grade(self):
    if self.score>=80:
        return 'A'
    return 'B'
    
#定义一个类
class Person(object):
    def __init__(self, name,score):
        self.name=name
        self.score=score
        
p1=Person('Bob',90)
#动态将方法绑定到实例上
p1.get_grade=types.MethodType(fn_get_grade,p1,Person)
print p1.get_grade() #这里正常

p2=Person('xiaohong',100)
print p2.get_grade() #这里报错，因为p2没有绑定这个方法