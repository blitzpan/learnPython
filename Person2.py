# -*- coding:utf-8 -*-
class Person(object):
    address='earth'  #�����ԣ�����ͨ�����������з��ʣ�Ҳ����ͨ��ʵ���������з���
    count =0
    def __init__(self, name, score):
        self.name=name
        self.__score=score

p = Person('Bob', 59)

print p.name
#print p.__score
print '-----------'
print Person.address
print p.address
print Person.count
print p.count
print '-----------'
p.address='china'
print Person.address
print p.address
p.count=10
print Person.count
print p.count
print '-----------'
Person.address='123'
print Person.address
print p.address
Person.count=7
print Person.count
print p.count