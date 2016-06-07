# -*- coding:utf-8 -*-
print("匿名函数：")
f = lambda x:x*x
print(f(5))

print("匿名函数作为返回值：")
def build(x,y):
	return lambda :x*y
f = build(3,5)
print(f())