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
#### 错误处理

`try...except ...finally`

`BaseException`：是所有错误类的父类。

```
# -*- coding:utf-8 -*-
try:
    print('try...')
    r = 10/1
    print('result=', r)
except ValueError as e:
    print('ValueError:' , e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('如果添加了else，并且程序没有错误的话，执行else语句。')
finally:
    print('finally...')
print('END')
```
[常见的错误类型和继承关系](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

> 如果错误没有被捕获，它会一直往上抛，最后被Python解释器捕获，打印一个错误信息。


##### 记录错误

> Python内置的`logging`模块可以非常容易得记录错误信息。

```
print('打印日志：')
import logging
try:
    print(10/0)
except Exception as e:
    logging.exception(e) # 不知道这个记录到哪里去了，可能还需要配置
finally:
    print('End')
```
##### 抛出错误
> 可以根据需要，定义一个错误的class，确定继承关系，然后用`raise`语句抛出一个错误实例。

```
print("抛出异常：")
class FooError(ValueError):
    pass
    
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value:%s' % s)
    return 10/n
foo('0')
```

> 将异常抛给父方法

```
try:
	pass
except ValueError as e:
	print('error')
	raise # 没有参数，将这个异常原样抛出
	raise FooException('...') # 将异常转换后抛出
```

#### 调试
要想比较爽的进行设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好用的Python IDE有[`PyCharm`](http://www.jetbrains.com/pycharm/)。
Eclipse加上[pydev](http://pydev.org/)插件也可以调试Python程序。
##### 断言`assert`
* 如果断言结果为`True`，那么继续往下走。
* 如果断言结果为`False`，那么抛出`AssertionError`异常。
* 启动Python解释器时可以用-O参数来关闭assert。

```
# -*- coding:utf-8 -*-
print('使用断言来进行调试：')
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10/n

foo('0')
```

##### logging
* 指定记录信息的级别：`debug，info，warning，error`

```
print('通过logging来调试：')
import logging
logging.basicConfig(level=logging.INFO) #定义logging的输出级别
s = '0'
n = int(s)
logging.info('n=%d' % n)
print(10/n)
```

##### pdb
> Python的调试器pdb，让程序以单步方式运行。通过命令行pdb的方式太麻烦了，所以不采用。

* `1`:查看代码。
* `n`:单步执行代码。
* `p 变量名`:查看变量。
* `q`:结束调试。

##### pdb.set_trace()
> 使用pdb.set_trace()不需要单步执行，只需要引入import pdb，然后再可能出错的地方添加`pdb.set_trace()`，就可以设置一个断点。

*这种方法比单步好用了一些，但是也好用不到哪里去。*

```
print('通过pdg.set_trace()来进行调试：')
import pdb
s = "0"
n = int(s)
pdb.set_trace() # 程序到这里自动暂停
print(n)
print(10/n)
```
#### 单元测试
`TDD:Test-Driven Development`：测试驱动开发。
* test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不执行。
* `assertEqual()` ：断言结果是否相同
* `assertRaises(KeyError)`：断言期待抛出指定类型的Error。

**被测试类`mydict.py`** 
```
# -*- coding:utf-8 -*-
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value
```
**测试类`mydict_test.py`**
```
# -*- coding:utf-8 -*-
import unittest #引入单元测试模块
from mydict import Dict
class TestDict(unittest.TestCase): #测试类从unittest.TestCase继承
    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__=='__main__':
    unittest.main() # 运行测试类
```

##### 运行单元测试
* 简单的方法就是在单元测试类后面添加两行
```
if __name__ == '__main__':
    unittest.main()
```
* 在命令行通过参数`-m unittest`直接运行单元测试
`$ python3 -m unittest mydict_test`
> 这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。

##### `setUp` 和 `tearDown`
> 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码。


```
class TestDict(unittest.TestCase): #测试类从unittest.TestCase继承
    def setUp(self):
        print('begin:')
    def tearDown(self):
        print('end')
```

#### 文档测试
这个估计也用不到，不想看就不看了。能力差还任性，就这么着了。

### IO编程

> 由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。譬如：CPU输出100M需要0.01秒，磁盘接收数据需要10秒。怎么办呢？有两种办法。

* 同步IO。CPU等着，程序暂停执行后面代码，等待数据写入磁盘之后，接着往下面执行。
* 异步IO。CPU接着干下面的事情，磁盘慢慢写。
	> 异步的编程麻烦，因为大多数情况下保存完数据都需要知道保存是否成功。
	
	* 一种是保存完了返回来告诉你，这是**回调模式**。
	* 一种是你不断的检查，这是**轮询模式**。

> 这里的IO编程例子都是同步模式。


#### 文件读写
* 自己实现打开关闭文件：
```
print('读文件：')
try:
    f = open('D:/lifeIsTough/learnPython/IOTest/testFile.txt','r')
    content = f.read()
    print(content)
finally: #文件必须关闭，finally防止出现异常，文件没有关闭的情况
    if f:
        f.close()
```
* 系统自动关闭文件，使用with语法不用自己调用close方法：
```
print('with语法自动关闭文件。')
with open(filePath, 'r') as f:
    print(f.read())
```
> `read()`读取文件所有内容，容易造成内存溢出。
> `read(size)`方法每次调用size个字节的内容。
> `readline()`每次读取一行。
> `readlines()`一次读取所有行并返回list。

> 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便。

```
print('readline：')
with open(filePath, 'r') as f:
    oneL = f.readline().strip()
    while oneL != '':
        print(oneL) #把末尾的\n去掉
        oneL = f.readline().strip()
```

##### 二进制文件
上面是读取utf-8编码的文本文件。如果要读取二进制文件，图片、视频等，用`rb`模式。
`f = open('/Users/michael/test.jpg', 'rb')`

##### 字符编码
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
`f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')`

##### 编码不规范文件
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
`f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')`

##### 写文件
> 唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件。
> w是覆盖写，a是追加写。

```
f = open('/Users/michael/test.txt', 'w') 
f.write('Hello, world!')
f.close()
```
> 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险。

```
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```
> 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。


#### StringIO和ByteIO

> StringIO就是在内存中读写str。

```
print('写入StringIO：')
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue()) #获取写入后的str
#
print('读取StringIO：')
f = StringIO('Hello!\n Hi!\nGoodBye!')
while True:
    s = f.readline()
    if s=='':
        break
    print(s.strip())
```
##### BytesIO
StringIO只能是str，如果要操作二进制数据，就需要使用BytesIO。

```
print('写入BytesIO：')
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) #注意，这里写入的不是str，而是tytes
print(f.getvalue())
#b'\xe4\xb8\xad\xe6\x96\x87'

#
print("读取BytesIO:")
from io import StringIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
content = f.read()
print(content)
print(content.decode('utf-8'))
```





#### 操作文件和目录

> Python 内置的os模块可以直接调用操作系统提供的接口函数来操作文件。

* 判断操作系统的类型
> 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

```
import os
os.name
```

* 获取系统详细信息：os.uname()
> windows没有这个函数

```
os.uname()
```

* 环境变量

```
os.environ
#获取某个环境变量的值：
os.environ.get('PATH')
os.environ.get('x', 'default')
```

##### 操作文件和目录
> 函数一部分在`os`模块下，一部分在`os.path`模块下。

```
print("操作文件和目录：")
#
print("查看当前目录的绝对路径：")
import os,os.path
print(os.path.abspath('.'))
print("在某个目录下创建一个新目录：")
#创建一个目录
#os.mkdir('d:/testDir') #当已经存在的时候，再次创建会报错
#先把新目录的完整路径表示出来：
newPath = os.path.join('d:/testDir','test1') #用这种方法来获取一个路径，可以正确处理不同的操作系统的路径分隔符。Linux返回/，windows返回\
# 但是注意，盘符后面的是/
print(newPath)
os.mkdir(newPath)
#
print('删除一个目录：')
os.rmdir(newPath)
print('拆分路径，也不要直接拆分，要用os.path.split()，把路径拆分成两部分，后部分是目录或者文件名：')
pathArr = os.path.split(newPath)
print(pathArr)
#这些join合并、split拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

#
filePath = os.path.join('D:/testDir','test.txt')
print("文件重命名：")
# 重命名的路径如果和原路径不一致，那么是移动+重命名，如果不写路径，那么把文件移动到了当前程序所在的路径
os.rename(filePath,os.path.join('D:/testDir','test1.txt'))
```

* os模块没有文件复制，因为操作系统没有提供复制接口。可以通过文件读写来完成复制。也可以使用`shutil`模块的`copyfiles()`函数。
* `shutil`可以看做是os模块的补充。

```
print('列出当前目录的所有目录：')
dirs = [x for x in os.listdir('.') if os.path.isdir(x)] #遍历每一个元素，把符合的放入数组中
print(dirs)

#
print("列出所有的xml文件：")
files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.xml'] #获取所有以.xml结尾的文件
print(files)
```

* 实现`dir -l`

```
print('实现dir -l')
def dir_l():
    files = os.listdir('.')
    for f in files:
        if os.path.isdir(f):
            print('d', f)
        else:
            print('f', f)
while True:
    command = input("请输入命令：")
    if command=='q':
        print('退出！')
        break
    elif command=='dir -l':
        dir_l()
        break
    else:
        print("命令不存在！")
```

* 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

```
def findFile(curP, value):
    dirs = os.listdir(curP)
    for d in dirs:
        if os.path.isdir(d):
            findFile(os.path.join(curP,d), value)
        else:
            if value in d:
                print(os.path.join(curP,d))

findFile('.', '.xml')
```
#### 序列化
* 把变量从内存中变成可存储或传输的过程称之为序列化（pickling）。其他语言称之为serialization/marshalling/flattening等。
* 把序列化的对象重新读到内存里称之为反序列化（unpickling）。

> `pickle.dumps()`方法把任意对象序列化成types，然后把这个bytes写入文件。或者用另一个方法`pickle.dump()`直接把对象序列化后写入一个file-like object。

```
import pickle
print("序列化：")
print("将一个对象序列化，然后写入文件：")
d = dict(name='Bob', age=20, score=88)
dBytes = pickle.dumps(d) #dumps方法吧任意对象序列化成bytes。
print(dBytes)

#这是第一种写入：
#with open('d:/testFile.txt','wb') as f:
#    f.write(dBytes)

#这是第二种写入：
try:
    f = open('d:/testFile.txt','wb')
    pickle.dump(d, f) # 注意，这里是dump，而上面的是dumps
except Exception as e:
    print(e)
finally:
    f.close()
```

* 将对象从磁盘读到内存中，先把内容读到bytes，再用`pickle.loads()`方法反序列化出对象。或者用`pickle.load()`从file-like Object中直接反序列化出对象。

```
print("将对象从磁盘读到内存中：")
try:
    f = open('d:/testFile.txt','rb')
    d = pickle.load(f)
    print(d)
except Exception as e:
    print(e)
finally:
    f.close()
```

**注意：**
不同版本的Python的序列化彼此不兼容，所以，只能用Pickle保存那些不重要的数据，不能成功序列化也没关系的。

##### JSON

| JSON类型 | Python类型 |
| ---- | ---- |
|`{}`|`dict`|
|`[]`|`list`|
|`"string"`|`str`|
|`123.45`|`int/float`|
|`true/false`|`True/False`|
|`null`|`None`|

* 基础类

```
print("将对象转成json：")
import json
d = dict(name='Bob', age=20, score=88)
jsonRes = json.dumps(d)
print(jsonRes)
```
* 自定义类

```
print("将自定义类转成json：")
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('ZhangSan',18,88)
print(json.dumps(s)) # 这里直接报错，Student不是一个可序列化的对象。
```
* 自定义类正确转json


```
print("将自定义类转成json：")
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('ZhangSan',18,88)
#print(json.dumps(s)) # 这里直接报错，Student不是一个可序列化的对象。

#解决办法一：添加一个转换函数
def studnet2dict(std):
    return {
        "name":std.name,
        "age":std.age,
        "score":std.score
    }
print(json.dumps(s, default=studnet2dict))

#解决办法二：调用特殊属性
print( json.dumps(s, default=lambda obj:obj.__dict__) )
```
###### json反序列化
`loads()`方法先转换出dict对象，传入`object_hook`函数把`dict`转成`Student`实例。

```
print("json反序列化：")
def dict2studnet(d):
    return Student(d['name'],d['age'],d["score"])

jsonStr = '{"name":"Lisi","age":"28","score":"100"}'
s = json.loads(jsonStr, object_hook=dict2studnet)
print(s.name,s.age,s.score)
```

### 进程和线程
* 一个任务就是一个进程（`Process`），比如打开一个浏览器就是一个进程，打开一个word就启动一个word进程。
* 一个进程内部，会同时运行多个字任务，这些子任务就是线程（`Thread`）。 

如果我们想要执行多个任务怎么办？
* 多进程（每个进程有一个线程）
* 多线程（一个进程多个线程）
* 多进程+多线程（每个进程多个线程，这种模型比较复杂，很少使用）

#### 多进程

##### fork (创建子进程)
> Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

```
# -*- coding:utf-8 -*-
#
print("轻松创建子进程：fork函数会返回两次。")
import os
print('Process (%s) start...' % os.getpid())
# 只在Unix/Linux/Mac上面起作用，windows不能运行
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```
> 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

##### multiprocessing（跨平台版本的多进程模块）

> `multiprocessing`模块提供`Process`类来代表一个进程对象。

```
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    for x in range(10):
        print('    子进程%s(%s)' % (name, os.getpid() ))
        
if __name__=='__main__':
    print('父进程%s' % os.getpid())
    sonP = Process(target=run_proc, args=('son1',))
    sonP.start()
    sonP.join() #join使该进程执行完之后程序再往下执行
    print('子进程执行完成。')
```

##### Pool

> 如果要启动大量的子进程，可以用进程池的方式批量创建子进程。

* Pool不用start
* 调用Pool.join()方法会等待所有子进程执行完毕。
* 调用join之前必须调用close，调用close之后就不能新增Process了。
* Pool的默认大小是CPU的核数。

```
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    try:
        print('    子进程%s(%s)开始执行：' % (name,os.getpid()))
        start = time.time()
        time.sleep(random.random()*3)
        end = time.time()
        print('    子进程%s(%s)执行了%0.4f秒' % (name, os.getpid(), end-start))
    except Exception as e:
        print(e)

if __name__=='__main__':
    print('父进程%s开始执行：' % os.getpid())
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,) )
    print('等待所有进程执行完成')
    p.close()
    p.join()
    print('所有进程执行完成。')
```
##### 子进程
> 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还要控制子进程的输入和输出。
> `subprocess`模块可以让我们非常方便的启动一个子进程，然后控制其输入和输出。

**在Python代码中运行命令`nslookup www.python.org`**
```
# -*- coding:utf-8 -*-
#
print("子进程：")
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code', r)
```
**如果子进程还需要输入，则可以通过`communicate()`方法输入：**

```
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8')) #这一行报错了，无法继续执行
print('Exit code:', p.returncode)
```
上面的代码相当于在命令行执行命令nslookup，然后手动输入：
```
set q=mx
python.org
exit
```

##### 进程间通信
`multiprocessing`模块包装了底层的机制，提供了`Queue`、`Pipes`等多种方式来交换数据。

> 在Unix/Linux下，`multiprocessing`模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，**父进程所有Python对象都必须通过`pickle`序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。**

```
# -*- coding:utf-8 -*-
# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

print('以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：')

#写数据进程执行的代码
def write(q):
    print("写进程：%s" % os.getpid())
    for value in ['A','B','C','D']:
        print('把%s放入队列。' % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    print('读进程：%s' % os.getpid())
    while True:
        value = q.get(True)
        print('从队列中获取：%s' % value)
        
if __name__=='__main__':
    #父进程创建Queue，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程是死循环，无法等待其结束，只能强行终止：
    pr.terminate()
```



#### 多线程
> 两个多线程模块：`_thread`和`threading`。
* _thread：低级模块
* threading：高级模块，对_thread进行了封装，绝大多数只需要使用threading这个高级模块。

启动线程就是把一个函数传入并创建`Thread`实例，然后调用`start()`开始执行。

* 任何进程默认启动一个线程，这个线程是主线程，主线程可以启动新的线程。
* Python的threading模块有个`current_thread()`函数，永远返回当前线程的实例。
* 主线程实例的名字叫`MainThread`，子线程名字在创建的时候指定，不起名字默认`Thread-1`,`Thread-2`...

```
# -*- coding:utf-8 -*-
import time, threading
# 新线程执行的代码
def loop():
	print('线程%s运行中' % threading.current_thread().name)
	n = 0
	while n<5:
		n = n+1
		print("线程%s>>>%s" % (threading.current_thread().name, n))
		time.sleep(1)
	print("线程%s停止！" % threading.current_thread().name)	

print('线程%s正在运行中。。。' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('线程%s停止！' % threading.current_thread().name)

```
##### Lock

> 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

**一个错误的例子，这个的输出结果不一定为0**
```
# -*- coding:utf-8 -*-
import time, threading

#银行存款
balance = 0
def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n 
    #print(balance)
    
def run_thread(n):
    for i in range(100000): #共执行100000先存后取
        change_it(n)
    print('线程执行完成。')

t1 = threading.Thread(target=run_thread, args=(500,))
t2 = threading.Thread(target=run_thread, args=(800000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```
为什么会出现结果不为0的情况呢？
因为这两行语句执行的时候可能发生线程切换，导致结果不为0的情况。所以我们在一个线程修改balance的时候，要将balance锁定，使其他线程不能更改。

```
balance = balance + n
balance = balance - n 
```
> 如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现。

* 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
* 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
* 锁的坏处：
	* 首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
	* 可能引起死锁。

```
# -*- coding:utf-8 -*-
import time, threading

#银行存款（给线程加锁）
balance = 0
lock = threading.Lock()
def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n 
    
def run_thread(n):
    for i in range(100000): #共执行100000先存后取
        #先获得锁
        lock.acquire()
        try:
            change_it(n) #放心的改，这回不会因为多线程引起异常数据了
        finally:
            #改完了一定要释放锁
            lock.release()
    print('线程执行完成。')

t1 = threading.Thread(target=run_thread, args=(500,))
t2 = threading.Thread(target=run_thread, args=(800000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

##### 多核CPU

> 一个死循环线程会100%占用一个CPU。如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。

**由于GIL的存在，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。**

 
**用Python写个死循环：**
```
# -*- coding:utf-8 -*-
#
print('一个死循环的例子：')
import threading, multiprocessing
def loop():
	x = 0
	while True:
		print(x)

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()
```

**小结：**
* 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
* Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。


#### ThreadLocal
> 每个线程都有自己的数据，线程使用自己的局部变量比使用全局变量好，使用局部变量只有线程自己看见，不会影响其他线程，而全局变量的修改必须加锁。

全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

**小结：**
* 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
* 这个很有意思，还有详细的推导过程可以[看一下](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431928972981094a382e5584413fa040b46d46cce48e000)。

```
# -*- coding:utf-8 -*-
import threading
#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
	#获取当前线程关联的student
	std = local_school.student
	print('线程%s中的name=%s' % (threading.current_thread().name, std))
def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student=name
	process_student()
t1 = threading.Thread(target=process_thread, args=('Alice',))
t2= threading.Thread(target=process_thread, args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()

```



#### 进程vs.线程

> 要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。
* 如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
	* 多进程模式最大的**优点**就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的**Apache**最早就是采用多进程模式。
	* 多进程模式的**缺点**是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。
* 如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。
	* 多线程模式**致命的缺点**就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。
	* 在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。


##### 线程切换
操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。

所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。


##### 计算密集型 vs IO密集型
* **计算密集型任务：**特点是要进行大量的计算，消耗CPU资源。要最高效地利用CPU，**计算密集型任务同时进行的数量应当等于CPU的核心数**。
* **IO密集型任务：**涉及到网络、磁盘IO的任务都是IO密集型任务。常见的大部分任务都是IO密集型任务，比如Web应用。IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

##### 异步IO

考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单进程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程。

#### 分布式进程
这个感觉好屌的样子，虽然感觉一般用不上

* 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

* Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

`task_master.py`
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')
```
`task_worker.py`
```
# -*- coding: utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
```
*据说这个例子在mac上是没有问题的，但是在windows上无法正常运行。*
[解决办法看23楼](http://bbs.csdn.net/topics/390869705/)

`task_master.py`修改之后正常运行：
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager 

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

def return_task_queue():
	global task_queue
	return task_queue
def return_result_queue():
	global result_queue
	return result_queue

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def test():
	# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
	QueueManager.register('get_task_queue', callable=return_task_queue )
	QueueManager.register('get_result_queue', callable=return_result_queue)
	# 绑定端口5000, 设置验证码'abc':
	manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
	# 启动Queue:
	manager.start()
	# 获得通过网络访问的Queue对象:
	task = manager.get_task_queue()
	result = manager.get_result_queue()
	# 放几个任务进去:
	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %d...' % n)
		task.put(n)
	# 从result队列读取结果:
	print('Try get results...')
	for i in range(10):
		r = result.get(timeout=10)
		print('Result: %s' % r)
	# 关闭:
	manager.shutdown()
	print('master exit.')

if __name__=='__main__':
	freeze_support()
	test()

```

### 正则表达式

|表达式    |    含义    |
|---------|------------|
|``       |


##### re模块
因为Python的字符串本身就有`\`转义的功能，所以我们写的时候要注意：
```
s = `ABC\\-001`
#对应的正则表达式的字符串变成：
#ABC\-001
```
**因此强烈建议使用Python的`r`前缀，就不用考略转义的问题了：
```
s = r`ABC\-001`
#对应的正则表达式字符串不变
#ABC\-001
```

### 常用内建模块



