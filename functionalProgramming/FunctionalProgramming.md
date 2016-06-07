#函数式编程
> 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

##高阶函数
* 变量可以指向函数。
* 函数名其实就是指向了函数的变量。
如果把函数名指向了一个变量，那么就不能用改函数了。

```
abs=10
abs(-10)就会报错，要回复abs函数，只能重启了。
```

* 一个函数可以接收另一个函数作为参数，这种函数就成为高阶函数。

```
print("高阶函数：")
def add(x,y,f):
	return f(x)+f(y)

f=abs
print(add(-3,-5,f))
```
### map/reduce
`map`：函数接受两个参数，一个是函数，一个是`Iterable`，map将传入的函数依次作用到序列的每个元素上，并把结果作为新的Iterator返回。
```
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
```

`reduce`：把一个函数作用在一个序列`[x1,x2,x3,...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算，效果：
`reduce(f, [x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)`
```
print('reduce函数：')
from functools import reduce
def myAdd(x,y):
	return x+y
r = reduce(myAdd, l)
print(r)
print('当然求和可以直接使用sum方法：')
print(sum(l))
```








### filter
### sorted
## 返回函数
## 匿名函数
## 装饰器
## 偏函数


