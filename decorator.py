# -*- coding:utf-8 -*-
import functools
#1.ԭʼ
def f1(x):
    print 'call',x
print f1.__name__#��ӡ�����f1

#2.��decorator������£��ٴ�ӡ������
def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    print 'call f2',x
print f2.__name__#��ӡ�����wrapper

#3.functools���ƺ�����Ϣ
#��decorator������£��ٴ�ӡ������
def log3(f):
    @functools.wraps(f) #��f����������������Ϣ������wrapper������
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log3
def f3(x):
    print 'call f3',x
print f3.__name__#��ӡ�����wrapper




