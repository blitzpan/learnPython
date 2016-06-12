# -*- coding:utf-8 -*-

print("打印方法的名称：")
def now():
	print('now 方法内部。')
f = now
f()
print(now.__name__)
print(f.__name__)

print("定义一个打印日志的装饰器：")
def log(func):#接收一个函数作为参数，并返回一个函数
	def wrapper(*args, **kw):
		print("call %s():" % func.__name__)
		return func(*args, ** kw)
	return wrapper

@log
def test1():#把@log放在test1前面，那么调用test1的时候就相当于调用了log(test1)
	print("in test1")
test1()

print("装饰器本身带参数：")
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print("%s %s()" % (text,func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log('字符串参数')
def now():
	print("2015")
now()
print("这里的now函数的名称已经变了，这里不符合我们的要求。", now.__name__)

print("利用functools.wraps将原始函数的一些属性复制到wrapper函数中：")
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s:' % func.__name__)
	return wrapper
@log
def now():
	print("in now")
	
now()
print("方法名称：",now.__name__)
	
print("将带参数的decorator的一些属性复制到新方法中：")
def log(text):
	def decorator(func):
		@functools.wraps(func)#将func的一些属性复制到wrapper中
		def wrapper(*args, **kw):
			print("%s %s():" % (text,func.__name__))
			func(*args, **kw)
		return wrapper
	return decorator

@log('hehe')
def now():
	print("in now!")
now()
print("方法名称：", now.__name__)
	
#
print("请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。")
print('同时，改装饰者既支持有参数，也支持无参数。')
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call：', text)
            func(*args, **kw)
            print('end call')
        return wrapper
    #return decorator(text) if callable(text) else decorator
    if callable(text): # 这一种实现方式和上面的实现方式结果是一样的。
        return decorator(text)
    else:
        return decorator

@log
def f1():
    print('f without param')

@log('parm')
def f2():
    print('f with param')

f1()#相当于执行了 log(f1)
f2()#相当于执行了 log('parm')(f2)
	










	
	























			