# -*- coding:utf-8 -*-
import functools
#1.原始
def f1(x):
    print 'call',x
print f1.__name__#打印结果是f1

#2.有decorator的情况下，再打印函数名
def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    print 'call f2',x
print f2.__name__#打印结果是wrapper

#3.functools复制函数信息
#有decorator的情况下，再打印函数名
def log3(f):
    @functools.wraps(f) #将f函数的所有属性信息拷贝到wrapper方法上
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log3
def f3(x):
    print 'call f3',x
print f3.__name__#打印结果是wrapper




