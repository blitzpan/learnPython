# -*- coding:utf-8 -*-
print(abs)
#<built-in function abs>   可以看出abs是一个函数本身
print("高阶函数：")
def add(x,y,f):
	return f(x)+f(y)

print(add(-3,-5,abs))

print('map函数：')
def f(x):
	return x*x

l = [1,2,3,4,5,6,7,8,9]
r = map(f,l) #返回的r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(l)
print(list(r))

print('把这个list中的所有数字都转为字符串：')
r = list(map(str,l))
print(r)

print('reduce函数：')
from functools import reduce
def myAdd(x,y):
	return x+y
r = reduce(myAdd, l)
print(r)
print('当然求和可以直接使用sum方法：')
print(sum(l))

print('str转成int：')
def str2int(s):
	def fn(x, y):
		return x*10+y 
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn, map(char2num, s))
s = '13579'
s = str2int(s)
print(s)

print('使用lambda函数进一步简化：')
from functools import reduce
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2int(s):
	return reduce(lambda x,y:x*10+y, map(char2num,s))
r = str2int('13579')
print(r)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normaliza(name):












