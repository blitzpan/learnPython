# -*- coding:utf-8 -*-
#切片
L=[1,2,3,4,5,6,7]
print(L[0:3])#[0:3]前包后不包，取了0、1、2三个位置的三个数
print(L[-2:])#倒数第一个是-1
L100 = list(range(100))
print(L100)
#
print("前10个数，每两个取一个：")
print(L100[:10:2])
#
print("所有数，每五个取一个：")
print(L100[::5])
#
print("原样复制一个list：")
L100Copy = L100[:]
print(L100Copy)
#迭代
for ch in 'ABC':
    print(ch)
    

print("判断一个对象是否可迭代")
from collections import Iterable
print(isinstance('abc',Iterable)) # str是否可以迭代

print("迭代的时候同时访问索引和元素本身：")
#enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
    print(i,value)
print('在for循环中，同时引用两个变量')
for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)

for i,x in enumerate([(1,2),(3,4),(5,6)]):
    print(i,x[0],x[1])

#列表生成式
#
print('生成1到10=')
print(list(range(1,11)))
#
print('生成=[1x1, 2x2, 3x3, ..., 10x10]')
print("把要生成的元素x*x放前面，后面for循环，就可以把list创建出来。")
l=[x*x for x in range(1,11)]
print(l)
print("生成偶数的平方=")
l=[x*x for x in range(1,11) if x%2==0]
print(l)
print('两层循环生成排列=')
l=[m+n for m in 'ABC' for n in 'xyz']
print(l)
#
print("一行代码列出当前目录的所有文件和目录=")
import os
l=[d for d in os.listdir('.')]#os.listdir可以列出文件和目录
print(l)

#
print("列表生成式同时使用两个变量来生成list=")
d={"zhang":"zhangsan","li":"lisi"}
l=[k+'='+v for k,v in d.items()]
print(l)

#
print('把链表中的所有字符串变成小写=')
L = ["A",'B','C']
l = [s.lower() for s in L]
print(l)
#
print("列表生成式中使用if")
L = ['Hello', 'World', 18, 'Apple', None]
l=[s.lower() for s in L if isinstance(s,str)]
print(l)

#生成器
print("生成器定义=")
g=(x*x for x in range(1,10))
print(g)#打印出来的是一个对象，而不是具体的值
print('通过next来取值（没有的时候抛出异常）=')
print(next(g),next(g))
print('通过next来取值太变态了，可以通过for循环来取值=')
for n in g:
    print(n)

#输出斐波拉切数列
print("输出斐波拉切数列：")
def fib(num):
    c=0
    cur=1
    bac=0
    while c<num:
        yield cur
        temp=cur 
        cur=bac+cur
        bac=temp
        c = c+1
f=fib(6)
print(next(f))
print(next(f))
for v in f:
    print(v)
    
#输出杨辉三角
def yhsj(num):
    ol=[1]
    n=1
    while n<=num:
        print(ol)
        nl=[]
        nl
    
    
    
    
    
    
    
    
        

