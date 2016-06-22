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

#
print("获取斐波那契数列的一个切片：")
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): #索引
            a,b=1,1
            for x in range(n):
                a,b = b, a+b
            return a
        if isinstance(n, slice): #n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(a);
                a,b = b,a+b
            return L
f = Fib()
print(f[0:5])
print(f[:10])

#
print("__getattr__方法：")
class Student(object):
    def __init__(self,name):
        self.name = name

s = Student('ZhangSan')
print(s.name)
#print(s.sex) #类没有这个属性，那么会抛出异常

print("通过__getattr__()，动态返回一个属性：")
class Student(object):
    def __init__(self,name):
        self.name = name
    def __getattr__(self, attr):
        if attr=='sex':
            return '男'

s = Student("Wang")
print(s.name)
print(s.sex)
print(s.age) #我们明明没有定义age，但是这里也不会报错的，因为__getattr__默认返回的是None

print("也可以在getattr中返回一个方法，这个时候调用的也要做相应的改变：")
class Student(object):
    def __init__(self,name):
        self.name = name
    def __getattr__(self, attr):
        if attr=='sex':
            return '男'
        elif attr=='age':
            return lambda:25
            
s = Student("Zhang")
print(s.age()) #这个时候调用的不是属性而是方法

#
print("利用完全动态的__getattr__，写一个链式调用：")
class Chain(object):
    def __init__(self,path=""):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    
    __repr__ = __str__

print( Chain().status.user.timeline.list ) 

#
print("__call__方法：")
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print( 'My name is %s.' % self.name)
s = Student("ZhangSan")
s() #调用这个实例本身

#
print("判断一个变量是对象还是一个函数：callable")
print(callable(Student('Lisi'))) #True
print(callable(max)) #True
print(callable([1,2,3])) #False
print(callable(None)) #False
print(callable('str')) #False














	
