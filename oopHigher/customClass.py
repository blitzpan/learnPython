# -*- coding:utf-8 -*-
#
print("__str__方法：")
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'student[name:%s]' % (self.name)

s = Student("ZhangSan")
print(s)
#
print("__iter__()方法：斐波那契数列")
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self #实例本身就是迭代对象，返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a #返回下一个值
	
    def __getitem__(self, n): 
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
#for n in Fib():
#    print(n)
f = Fib()
print(f[10])
	
