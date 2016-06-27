# learnPython
[廖雪峰Python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

##Python基础
`#`开头是注释
`:`语句以冒号结尾，下面缩进的语句被视为代码块
```
a=100
if a>0:
	print(a)
else:
	print(-a)
```
###数据类型和变量
####字符串
特殊字符需要转义。
比如：
双引号里面又包含双引号。
```
"I'am \"ok\""
```
如果一个字符串中有很多字符需要转义，需要加很多`\`，为了简化，Python还允许用`r''`来表示，`''`内部的字符串默认不转义。
```
status = r'I'am "ok"'
```
用`'''...'''`的方式来表示多行内容。
```
print('''line1
line2
line3''')
```
####布尔值
`True``False`
布尔值可以用`and` `or` `not`运算。
####空值
`None`，`None`不能理解为0，因为0是有意义的，而`None`是一个特殊的空值。

**解释一下除法为什么也是精确的：**

Python中有两种除法：

* `/`的结果是浮点数，即使两个数可以整除，那么也是浮点数。
```
print(9/3)
3.0
```
* `//`地板除，其结果只取整数部分。

* 取余
```
>>> 10%3
1
```
**注意：**

* Python的整数没有大小限制。
* Python的浮点数也没有大小限制，但是超出一定范围就直接表示为`inf`(无限大)。

###字符串和编码

在最新的Python3版本中，字符串是以Unicode编码的，也就是说Python支持多语言。
`ord()`：获取字符的整数表示。
`chr()`：把编码转换成对应的字符。

```
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```
还可以用十六进制这么写str：
```
'\u4e2d\u6587'
'中文'
```
由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
bytes类型使用带b前缀的单引号或双引号表示：
`x=b'ABC'`

* `encode()`将str转成bytes：
```
'ABC'.encode('ascii')
'中文'.encode('utf-8')#中文不能转成ascii，因为中文编码超出了ascii最大编码范围
```

* `decode()`将bytes转成str：
如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法。
```
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
```



`len(str)`：计算str的字符数。
`len(b'ABC')`：计算字节数。
```
>>> len('中文')
2
>>> len('中文'.encode('utf-8'))
6
#可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
```

**注意**
* 为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
* Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。在文件开头写上这两行：
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
> 第一行告诉Linux/OS X系统，这是python可执行程序，而windows会忽略。
第二行告诉解释器，按utf-8读取文件。同时也必须保证使用的文本编辑器保存文件的时候使用的是utf-8无bom格式。


####格式化字符串输出
Python的格式化方法和C是一致的，用`%`实现。
如果只有一个`%?`，那么括号可以省略。

|%?  |          代表类型        |
|:----|:-----------------------|
|%d    |整数                   |
|%f    |浮点数                 |
|%s    |字符串                 |
|%x    |十六进制整数            |
|%%    |代表一个%               |
```
>>> '%2d-%02d' % (3,1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'
```


###使用list和tuple

* list
**有序集合**
```
# -*- coding:utf-8 -*-
#定义数组
classmates = ['zhang','sun','li']
print("链表=", classmates)
print("链表长度=", len(classmates))
print("访问链表中的第2个元素=", classmates[1])
print('链表追加一个元素')
classmates.append('追加的元素')
print("追加后=",classmates)
print('在第二的位置插入一个2')
classmates.insert(1,'2')
print('插入后=', classmates)
print("删除末尾元素pop")
classmates.pop()
print('删除末尾后=',classmates)
print('删除第二个元素')
classmates.pop(1)
print('删除第二个元素后=',classmates)
print("将第一个元素替成1")
classmates[0]=1
print("替换后=",classmates)
print('数组中的一个元素有是一个数组')
l1=[2.1,2.2,2.3]
l2=[1,l1,3]
print(l2)
print('访问2.2=', l2[1][1])
l=[]
print('空数组',l,len(l))
```

* tuple
**元祖：tuple一旦初始化就不能修改，没有insert/append等方法**
```
# -*- coding:utf-8 -*-
t=(1,2)
print("1 tuple=", t)
t=()
print('2 定义空的',t)
t=(1,)
print('3 只有一个元素的时候必须这么定义，否则当成小括号处理=',t)
```








###条件判断

```
# -*- coding:utf-8 -*-
age=20
if age>=18:
    print("可以枪毙了！")
    print("冒号下面所有缩进的代码是一个代码块。")
    
age=16
if age>=18:
    print("18岁以上")
elif age>14:
    print("大于14小于18岁")
else:
    print("还不满14岁")

l1 = []
print("对于0、空字符串、空list，都等于False")
if l1:
    print(True)
else:
    print(False)
    
print("输入进行if判断：")
birth=input("出生日期：")
#int()把一个字符串转成int类型
if(int(birth)<2000):
    print("00前")
else:
    print("00后")
    
    
```

###循环

* `for...in`循环
```
# -*- coding:utf-8 -*-
names=['zhang','li','wang']
for name in names:
    print(name)
print("求1到10的和。")
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print("1加到10=", sum)
```
`range()`：生成一个整数序列。
`list(range(5))`：range生成整数序列，然后通过list方法转换成list。
`range(5)`：生成从0开始小于5的整数。
```
#range
print(list(range(10)))
#求0到100的和：
print('求0到100的和：')
sum=0
for x in range(101):
    sum = sum + x 
print(sum)
```
* while循环
```
#求100以内所有奇数的和
sum=0
n=1 
while n<100:
    sum = sum+n
    n=n+2
print(sum)
```




###使用dict和set
####dict

字典类：dict(dictionary，其它语言中称为map)
```
# -*- coding:utf-8 -*-
#初始化
d={}
d={"li":"liSi",'wang':'wangWu'}
#新增
d['zhang']='zhangSan'
print(d['zhang'])
print(d['wang'])
```

**取值的时候，如果key不存在，那么会报错，解决办法:**

* `in`判断
```
#1. in操作
ifIn = 'zhang' in d
print(ifIn)
```


* `get`判断，如果key不存在，返回None，或者返回自定义值
```
#2. get操作：不存在返回None或者如果有默认值返回默认值
print(d.get('zhang'))
print(d.get('zhang1'))
print(d.get('zhang1','zhang1不存在。'))
```
####set
* set中的值不能重复。
* 使用list集合作为构造参数。

```
#set使用list操作构造参数
s=set([1,2,3])
print(s)
#set新增
s.add(4)
print(s)
#set删除
s.remove(4)
print(s)
#set求交集、并集
s2=set([3,4,5,6])
print("交集=", s & s2)
print("并集=", s | s2)
```  













## 函数
###调用函数

* `abs`：绝对值
* `max`：最大值
* `int`：转成int
* `float`：转成float
* `str`：转成字符串
* `bool`：转成布尔类型




###定义函数
* 使用`def`定义函数：
* 如果没有return语句，那么函数返回None。
* `return None`可以写成`return`
* >如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）。
####空函数pass
> pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
pass还可以用在其他语句里，缺少了pass，代码运行就会有语法错误。
```
def nop():
	pass
```
```
if age>=18:
	pass
```

####参数检查

```
# -*- coding:utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x 
    else:
        return -x 
        
print(my_abs(-5))
print(my_abs('a'))
```
####返回多个值
实际上是返回一个tuple，按位置赋值给接受的对象。
```
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
151.96152422706632 70.0
```
解一元二次方程：
```
#一元二次方程的解法
def quadratic(a,b,c):
    if a==0:
        return -c/b
    else:
        temp = math.sqrt(b*b-4*a*c)
        return (temp-b)/(2*a),(-temp-b)/(2*a)
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
```



###函数的参数

**总结**
* `*args`可变参数，args接受一个tuple
* `**kw`关键字参数，kw接受一个dict

####参数组合
Python中定义函数，参数定义的顺序是：*必选参数-默认参数-可变参数-命名关键字参数-关键字参数*

####默认参数
```
def people(name,sex='男',city='Beijing'):
```
调用的时候：
```
people('zhangsan')
#也可以将一个默认参数赋值，其他没有赋值的还是使用默认值
people('zhangsan',city='Tianjin')
```
**默认函数的坑：**
**定义默认参数要牢记一点：默认参数必须指向不变对象！**
[具体坑的案例](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000)
####可变参数
**参数的个数不确定**
* 参数作为一个list或者tuple传入，可以变相实现可变参数
```
def calc(numbers):
    sum=0
    for x in numbers:
        sum = sum+x*x 
    return sum 
print("可变参数第一种调用=",calc([1,2,3]))
```
* 真正的可变参数
```
print("把函数的参数改为可变参数：")
def calc(*numbers):
    sum=0
    for x in numbers:
        sum=sum+x*x 
    return sum 
print("可变参数调用1，传入任意个参数=",calc(1,2,3))
#在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
parm=[1,2,3]
print(calc(*parm))
```
####关键字参数

> 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
> 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

```
print("关键字参数：")
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
    if 'city' in kw:
        print('处理city信息')
    if 'job' in kw:
        print('处理job信息')

person('Tom',30)
extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)
```
####命名关键字参数
```
#限制调用者传入的关键字参数的名字
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)
#命名关键字参数在调用的时候必须传入参数名
person('Jack', 24, city='Beijing', job='Engineer')
#下面这个定义，由于命名关键字参数city有默认值，所以可以不传入city
def person(name, age, *, city='Beijing', job):
    pass
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    pass
```










###递归函数
```
# -*- coding:utf-8 -*-
def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n
print(fact(100))
```
**函数调用时通过栈stack这种数据结构实现的，每进入一个函数调用，就会加一层栈帧，由于栈的大小不是无限的，所以递归调用的次数过多，会导致栈溢出。**
**使用尾递归可以防止栈溢出（遗憾的是，大多数编程语言没有针对尾递归做优化，Python也没有优化），所以尾递归也会导致栈溢出**
**汉诺塔**
```
# 汉诺塔
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)#只有一个直接移动
    else:
        move(n-1,a,c,b)#将n-1个从a移动到b上
        print(a,'-->',c)#将第n个从a移到c上
        move(n-1,b,a,c)#将n-1个从b移到c上
move(3,'A','B','C')
```

##高级特性
###切片(slice)
```
# -*- coding:utf-8 -*-
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
```
> Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

###迭代
> Python对于dict的迭代是作用在key上的，如果要迭代value

```
for value in d.values()
```

> 如果要迭代key和value，可以用

```
for k,v in d.items()
```

> 字符串也是可以迭代的


```
for ch in 'ABC':
    print(ch)
```


```
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
```


###列表生成式
**根据一定规则快速生成一个list**
```
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
```










###生成器
> 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator。
> 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。
> 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


```
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
```

**简化上面例子**

```

```










###迭代器
##函数式编程
###高阶函数
####map/reduce
####filter

> 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

```
# -*- coding:utf-8 -*-
print("在一个list中，删掉偶数，只保留奇数。")
def is_odd(n):
    return n%2==1
L = [0,1,2,3,4,5,6,7,8,9]
l = list(filter(is_odd, L))
print(l)
#
print('把一个序列中的空字符串删掉。')
def not_empty(s):
    return s and s.strip() # and 主要是处理None情况
l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l)

``` 

**注意：**

声明：s为字符串，rm为要删除的字符序列

|    |    |
|:----|---- |
|s.strip(rm)|        删除s字符串中开头、结尾处，位于 rm删除序列的字符|
|s.lstrip(rm)|       删除s字符串中开头处，位于 rm删除序列的字符|
|s.rstrip(rm)|      删除s字符串中结尾处，位于 rm删除序列的字符|
|      |当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')|

```
print('求出全体素数。')
#先构造一个从3开始的奇数序列：
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#定义一个筛选条件：
def _not_divisible(n):
    return lambda x:x%n>0 #不能被整除返回true
def primes():
    yield 2
    it = _odd_iter() #初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
for n in primes():
    if n<1000:  #由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
        print(n)
    else:
        break 
```

```
print('计算回数：')
def is_palindrome(n):
    n = str(n)
    i=0
    while i<len(n)/2:
        if n[i]!=n[-1-i]:
            return False
        i=i+1
    return True
    
output = filter(is_palindrome, range(1,1000))
print(list(output))
#计算回数简化版：
def is_palindrome(n):
    n=str(n)
    return n[:] ==n[::-1]
```

***n[:] ==n[::-1]***简直是6翻了，-1就是从后往前，一个一个递减。


####sorted
```
print("对list进行排序；")
L = [36,5,-12,9,-21]
l = sorted(L)
print(l)
```
sorted()函数也是一个高阶函数，它可以接收一个key函数来实现自定义的排序。

> key函数作用在list的每一个元素上，并根据key函数的返回结果进行排序

```
print("按照绝对值大小进行排序：")
l = sorted(L, key=abs)
print(l)
```
对字符串排序：
```
print("对字符串排序：")
L = ['bob', 'about', 'Zoo', 'Credit']
l = sorted(L)
print(l)
```
字符串忽略大小写进行排序：
```
print("字符串忽略大小写进行排序：")
l = sorted(L, key=str.lower)
print(l)
```
反向排序：
> 传入第三个参数`reverse=True`即可。

```
print("反向排序：")
l = sorted(L, key=str.lower, reverse=True)
print(l)
```
```
print("按学生姓名排序：")
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return str.lower(t[0])
L2 = sorted(L, key=by_name)
print(L2)
#
print("按照学生成绩排序：")
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)
```


###返回函数
> 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

在一个函数内部定义另一个函数，并且将这个内部函数作为返回值返回。
* 内部函数可以使用外部函数的参数和局部变量。
* 但内部函数被返回时，相关的参数和变量都保存在返回的函数中，这种称为“闭包Closure”的程序结构拥有极大的威力。

```
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
```

**注意事项：**返回函数不要饮用任何循环变量，或者是后续会发生改变的变量。
如下面这个例子
```
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
```
可能你以为会输出1,4,9，但是实际结果是9,9,9。原因，返回的函数引用了变量i，而当返回的函数执行的时候，i已经变成了3。所以这里输出的是999。

如果一定要使用循环变量怎么办呢？那么就在创建一个函数，将这个循环变量作为参数传入。这样会使代码变长，可利用lambda函数缩短代码。
```
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
```













###匿名函数
> lambda表示匿名函数，冒号前面的x表示函数参数，匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

```
# -*- coding:utf-8 -*-
print("匿名函数：")
f = lambda x:x*x
print(f(5))

print("匿名函数作为返回值：")
def build(x,y):
	return lambda :x*y
f = build(3,5)
print(f())
```





###装饰器

```
print("打印方法的名称：")
def now():
	print('now 方法内部。')
f = now
f()
print(now.__name__)
print(f.__name__)
```

```
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
```





###偏函数

> 偏函数`functools.partial`的作用：把一个函数的某些参数给固定住（也就是设置了默认值），返回一个新函数，调用这个函数会更简单。

> 通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
```
#偏函数partial
print('把字符串转成数字：')
print(int('123456'))
print(int('123456',base=8))
print(int('123456',16))
```
当进制进行改变的时候，我们传入一个8或者16就可以实现了，但是如果我们特别懒，连一个8也不想传入，那么我们可以创建一个偏函数，直接调用这个函数默认就是按8进制处理字符串，然后返回10进制数字。
```
print('偏函数：')
import functools
int2 = functools.partial(int, base=2) #2进制的字符串转换成10进制输出
print(int2('100000'))
```


创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数。
```
int2 = functools.partial(int, base=2)
int2('10000')
#相当于调用
kw={'base': 2}
int('10000',**kw)
``` 
```
max2=functools.partial(max, 10)
max2(5,6,7)
相当于调用
args=(10,5,6,7)
max(*args)
```




##模块

> 一个.py文件就称为一个模块。

> 模块外面有包名Package。这样可以保证所有模块不冲突。本来abc模块，现在变成myPackage.abc模块。

> 每一个包目录下面都会有一个`__init__.py`文件，这个文件必须存在，否则Python会把这个目录当成普通目录，而不是一个包。`__init__.py`本身就是一个模块，而它的模块名就是包名。

> 不能和Python自带的模块名冲突。例如，系统自带了sys模块，自己的模块就不能命名sys.py，否则无法导入系统自带的sys模块。



###使用模块
```
# -*- coding:utf-8 -*-

'a test module' #模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__='god pan' #把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import sys
def test():
    args  = sys.argv #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    #命令行测试，打开改文件夹，按住shift，右键点击在此打开命令行窗口，然后执行python moduleTest1.py hehe
    print(args)
    if len(args)==1:
        print('Hello world！')
    elif len(args)==2:
        print('hello,%s' % args[1])
    else:
        print('太多的参数！')

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()
```

####作用域

> 正常函数和变量都是公开的。
> `__xxx__`这样的变量可以被直接引用，但是有特殊用途，如`__author__`,`__name__`,`__doc__`可以获取到模块描述信息。
> `_xxx`和`__xxx`变量是非公开的，不应该被直接引用（并不是不能，如果你硬是引用也没办法）。





###安装第三方模块

> 安装第三方模块，是通过包管理工具pip完成的。
> 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了（Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。）。如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path。
> 在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。
> 第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow。`pip install Pillow #如果没有安装这个模块需要先安装`

```
print('调用第三方模块生成缩略图：')
from PIL import Image
im = Image.open('D:/lifeIsTough/learnPython/module/test.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('D:/lifeIsTough/learnPython/module/thumb.jpg','JPEG')
```

> 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错。
> 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中。
```
import sys
sys.path
```

> 如果我们要添加自己的搜索目录，有两种方法：
* 一是直接修改sys.path，添加要搜索的目录：
```
import sys
sys.path.append('/users/hellow.py')
```
* 第二种方法是设置环境变量PYTHONPATH。Python自己本身的搜索路径不受影响。



##面向对象编程

```
# -*- coding:utf-8 -*-
print("定义一个学生类：")
class Student(object):
    def __init__(self,name,score):#第一个参数是self，表示实例本身
        self.name=name
        self.score=score
    
    def print_score(self):
        print('%s:%s' % (self.name, self.score))

print("创建学生实例并输出成绩：")
bart = Student('Bart',59)#不需要传入self
lisa = Student('Lisa', 87)

if __name__=='__main__':
    lisa.print_score()#也不需要传入self
    bart.print_score();
    bart.sex='男'#自由的给实例添加属性，或者通过构造方法
```

* `Student(object)`：表示该类是从object类继承过来。
* 

###类和实例


###访问限制

* 让内部属性不被外部访问，可以把属性的名称前加两个下划线`__`，以两个下划线开头的变量是私有变量，只能内部访问。
* **注意：**以双下划线开头，并以双下划线结尾的变量，是特殊变量，**特殊变量可以直接访问**。
* 单下划线开头的变量，可以在外部访问，但是约定俗成，把这种变量当成私有变量，不要随便访问。

```
print('创建私有变量：')
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))
        
tom = Student('Tom', 18)
tom.print_score()
#print(tom.__name) #这里报错，说没有__name属性
tom.__name='123'
tom.print_score()
print(tom.__name) #这里却没有报错，因为上面我们给这个实例一个__name属性
```


### 继承和多态

```
print('继承和多态：')
print('定义animal类：')
class Animal(object):
    def run(self):
        print('Animal is running...')
print("定义Dog和Cat类：")
class Dog(Animal):
    pass
class Cat(Animal):
    def run(self):#重写父类的方法
        print('Cat is running...')
    def eat(self):
        print('Cat is eating...')

dog = Dog()
cat = Cat()
dog.run()
cat.run()

print('判断一个变量是否是某种类型：')
print(isinstance(dog,Animal)) #True
print(isinstance(dog, Cat)) #False
```


### 获取对象信息

#### 使用type()

```
print('使用type()判断对象类型：')
print(type(123))
print(type('123'))
print("是否是字符串类型：", type('123')==str)
print(type(None))
print('使用type()来判断函数：')
print(type(abs))
print('判断一个对象是否是函数，用types模块中定义的常量：')
import types
def fun():
    pass
print( type(fun)==types.FunctionType ) #True
print( type(abs)==types.BuiltinFunctionType ) #True
print( type(lambda x:x)==types.LambdaType ) #True
print( type(x for x in range(10))==types.GeneratorType ) #True
```
#### 使用isinstance()

```
print('使用isinstance()：')
print(isinstance('abc', str))
print('判断一个变量是否在某些类型中：')
print( isinstance([1,2,3], (list,tuple)) )
```

#### 使用dir
> 使用dir获得一个对象的所有属性和方法，它返回一个包含字符串的list。

```
print("使用dir()：")
print( dir('abc') )
```
> 上面例子输出的方法有一个`__len__`，该方法是字符串的一个特殊方法，返回长度。如果你使用len()来获取一个对象的长度的时候，实际上len()函数内部，自动去调用了该对象的__len__()方法。如果我们自己定义的类想要使用len()来输出长度的话，那么可以为我们的类实现__len__()方法。

```
class MyObj(object):
    def __len__(self):
        return 100

print("自定义对象的长度=", len(MyObj()) )
```

#### 方法`getattr()`/`setattr()`/`hasattr()`

```
#getattr/setattr/hasattr
mo = MyObj()
if hasattr(mo, 'x'):#有属性'x'吗
    print('有属性x')
    print(mo.x)
else:
    print('没有属性x')
    setattr(mo, 'x', 10) #设置属性x
if hasattr(mo, 'x'):#有属性'x'吗
    print('有属性x')
    print(mo.x)
    print( getattr(mo, 'x') )

print('获取一个不存在的属性，会抛出异常：')
#getattr(mo, 'y')
print( getattr(mo, 'y', 404) )  #设置默认值，如果该属性不存在，那么返回一个默认值

#
print('获取一个对象的方法：')
fn = getattr(mo, 'print')
fn() #相当于调用了mo.print()
```



#### 实例属性和类属性

* 给*实例*绑定属性：通过*实例变量*，或通过*self变量*。
* 给*类*绑定属性：直接在class中定义属性。

```
print("实例属性、类属性：")
class Student(object):
    country='中国' #类属性
    def __init__(self,name):
        self.name=name #实例属性
li = Student('Li')
print(li.country, li.name)
print('打印类属性和实例属性：')
print(Student.country, li.country)
li.country = '我是中国人' #给实例一个country属性
print(Student.country, li.country)#会发现同名的实例属性和类属性同时存在
del li.country #删除实例属性
print(Student.country, li.country) #类属性仍然存在
```
**注意：**在开发中，千万不要让实例属性和类属性相同，相同的实例属性会屏蔽类属性，当实例属性删除之后类属性才起作用。

### 面向对象高级编程
#### 使用`__slots__`
* 运行时给实例添加属性和方法。
* `__slots__`定义的属性只对当前类实例起作用，对继承的子类是不起作用的。
* 除非子类也定义了`__slots__`，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`


```
# -*- coding:utf-8 -*-

class Student(object):
    pass

print("给实例添加属性：")
s = Student()
s.name='zhang'
print(s.name)

print('给实例添加方法：')
def setAge(self, age):
    self.age = age
from types import MethodType
s.setAge = MethodType(setAge, s) #给实例绑定一个方法
s.setAge(50) #调用绑定的方法
print(s.age)

print('给一个实例绑定的方法，对另一个实例是不起作用的，所以我们需要给类绑定方法：')
Student.setAge = setAge
s1 = Student()
s1.setAge(10)
print(s1.age)

#
print('我们不想让每个人都能随便的改实例的属性怎么办？添加__slots__，限制动态添加的属性名')
class Student(object):
    __slots__=('name','sex')#限制只能有这些属性
s = Student()
s.name='ZhangSan'
s.sex="男"
#s.age=18 #这里就会报错，Student没有age这个属性。

```

```
#
class GraduateStu(Student):
    pass
g = GraduateStu()
g.age = 18 #如果子类没有__slots__，那么父类定义的对子类不起作用
print(g.age)
#
class GraduateStu(Student):
    __slots__=('birth')
    pass
g = GraduateStu()
g.name = 18 #如果子类有__slots__，那么真正的slots是父子类相加。
print(g.name)
```

#### 使用`@property`

> `@property`本身是一个装饰器，相当于给一个属性添加get方法。
> `@score.setter`给属性score添加set方法。
> 如果让一个属性只读，那么不配置setter方法即可。

```
# -*- coding:utf-8 -*-
class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("必须是数字类型！")
        if value<0 or value>100:
            raise ValueError("必须在0到100之间！")
        self.__score = value

s = Student()
s.score = 100 #对外是直接操作了变量score，实际上我们是调用了一个set方法，那么在这个方法中，我们就可以对set的值进行一系列的校验。
print(s.score)
#s.score = "zhangsan" #会抛出异常
```

```
#
print('请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：')
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    @property
    def resolution(self):
        return self.__width * self.__height

s = Screen()
s.width=1024
s.height=768
print(s.resolution)
```

#### 多重继承
> Python允许使用多重继承，而Java语言只允许单一继承。

```
class CA(object):
	pass

class CB(object):
	pass

class Son(CA,CB):
	pass
```
 
#### 定制类
> 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

* `__str__`

```
print("__str__方法：")
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'student[name:%s]' % (self.name)

s = Student("ZhangSan")
print(s)
```

* `__iter__`

> 如果一个类想被用于`for...in`循环，那就必须实现一个`__iter__()`方法，该方法返回一个迭代对象，然后for循环会不断调该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环。

```
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

for n in Fib():
    print(n)
```

* `__getitem__`取迭代器的某一个值

> Fib虽然能作用于for循环，看起来和list有点像，但是不能像list一样直接取某一个值，Fib()[5]便会报错。实现`__getitem__()`就可以像list一样操作迭代器。

*其实自我感觉这个方法性能挺低的，因为调用这个方法每次都是从头到尾重新计算一次，然后把当前值的结果返回*

```
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
```

* `__getitem__()`传入的参数可能是一个`int`，也可能是一个切片对象`slice`（没有对切片的第三个参数做处理，也没有对负数做处理，如果涉及的话，还要更改好多）。
> 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

```
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
```

* `__getattr__`

> 调用一个属性的时候，首先直接找该属性，如s.name，当找不到该属性的时候，才到getattr中找。

> 可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

```
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
```

```
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
```

* `__call__`

> 通过__call__方法，直接在实例本身上调用。

```
print("__call__方法：")
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print( 'My name is %s.' % self.name)
s = Student("ZhangSan")
s() #调用这个实例本身
```

```
print("判断一个变量是对象还是一个函数：callable")
print(callable(Student('Lisi'))) #True
print(callable(max)) #True
print(callable([1,2,3])) #False
print(callable(None)) #False
print(callable('str')) #False
```
**其实callable并不能准确的判断一个变量是对象还是方法。因为有的对象也能被调用。**



#### 使用枚举类
**枚举类刚开始就掉入了坑里：**
我写了一个enum.py的测试类，然后写了简单的两行代码，怎么弄也不能运行，一直抱导入错误，最后终于发现原因了。
*我自己定义的文件名是enum*，和系统自带的重复了。
下面是这个错误的例子：
```
# -*- coding:utf-8 -*-
from enum import Enum

print("定义一个月份的枚举：")
Month = Enum('Month', ('Jan','Feb','Mar','Apr','May','Jun','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.item():
    print(name,'==>',member,',',member.value)
#报错：
Traceback (most recent call last):
  File "D:\lifeIsTough\learnPython\oopHigher\enum.py", line 2, in <module>
    from enum import Enum
  File "D:\lifeIsTough\learnPython\oopHigher\enum.py", line 2, in <module>
    from enum import Enum
ImportError: cannot import name 'Enum'
请按任意键继续. . .
```
**然后我把文件名由enum.py改成enumTest.py**
```
# -*- coding:utf-8 -*-
from enum import Enum

print("定义一个月份的枚举：")
Month = Enum('Month', ('Jan','Feb','Mar','Apr','May','Jun','Aug','Sep','Oct','Nov','Dec'))
#枚举所有的成员：
for name,member in Month.__members__.items():
    print(name,'==>',member,',',member.value)
print(Month.Feb, Month.Feb.value)

#输出结果如下：
定义一个月份的枚举：
Jan ==> MonthTest.Jan , 1
Feb ==> MonthTest.Feb , 2
Mar ==> MonthTest.Mar , 3
Apr ==> MonthTest.Apr , 4
May ==> MonthTest.May , 5
Jun ==> MonthTest.Jun , 6
Aug ==> MonthTest.Aug , 7
Sep ==> MonthTest.Sep , 8
Oct ==> MonthTest.Oct , 9
Nov ==> MonthTest.Nov , 10
Dec ==> MonthTest.Dec , 11
MonthTest.Feb 2
如果想要更精确的控制枚举类型，可以从`Enum`派生出自定义类：
请按任意键继续. . .
```
我们可以通过`Month.Jan`来引用一个常量。
> value属性是自动赋值给成员的int常量，默认从1开始计数。

**如果想要更精确的控制枚举类型，可以从`Enum`派生出自定义类：
from enum import Enum, unique

```
print("如果想要更精确的控制枚举类型，可以从`Enum`派生出自定义类：")
from enum import Enum, unique
#unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
	Sun=0 #Sun的value被设定为0
	Mon = 7
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6 
    
day1 = Weekday.Mon
print(day1)
print(Weekday['Tue'])
print(Weekday(7)) #Weekday.Mon，这里括号里面的值对应的是Mon=后面的值，而不是数组，切记
print(day1 == Weekday.Mon)
print(day1==Weekday(1)) #这里会报错，因为1找不到
```

#### 使用元类
##### type
**hello.py**
```
# -*- coding:utf-8 -*-
class Hello(object):
    def hello(self,name='world'):
        print('Hello, %s' % name)
```
**helloTest.py**
```
# -*- coding:utf-8 -*-
from hello import Hello
h = Hello()
h.hello()

print(type(Hello)) 
print(type(h))
输出：
Hello, world
<class 'type'> #表明这是一个类
<class 'hello.Hello'> #表明这是hello模块（文件名就是模块名）的一个Hello实例
请按任意键继续. . .
```

* type()函数可以查看一个类型或者变量的类型。
* type()函数可以不用通过class来创建出新的类型。

要创建一个class对象，type()函数依次传入3个参数：
* class的名称；
* 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
* class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

> type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类.

```
# -*- coding:utf-8 -*-

def fn(self, name='world'): # 先定义函数
    print('Hello, %s' % name)
    
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# 输出
Hello, world
<class 'type'>
<class '__main__.Hello'>
请按任意键继续. . .
```

##### metaclass
> 出了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
> metaclass，直译为元类：先定义metaclass，就可以创建类，最后创建实例。
> 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

*metaclass是Python里面最难理解，也是最难使用的魔术代码，正常情况下，不会用到，所以不学也可以。*

元类没有学习。
### 错误、调试和测试
####错误处理