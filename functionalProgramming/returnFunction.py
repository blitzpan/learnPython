# -*- coding:utf-8 -*-
print("直接求和：")
L = list(range(0,101))
def calc_sum(*args):
	ax=0
	for n in args:
		ax = ax+n
	return ax
print(calc_sum(1,2,3))
#
print("延迟加载求和：")
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax+n
		return ax
	return sum

f = lazy_sum(1,2,3)
print(f()) 

print("一个陷阱：")
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3 = count()#这里将count()的三个返回值分别赋值给了f1,2,3
print(f1())
print(f2())
print(f3())


print("返回函数中就是用到了循环变量：")
def count():
	fs=[]
	def g(j):
		def f():
			return j*j
		return f
	for i in range(1,4):
		fs.append(g(i))#g()函数会立刻执行，而g函数会返回一个函数
	return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
















