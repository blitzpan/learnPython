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
####sorted
###返回函数
###匿名函数
###装饰器
###偏函数
##模块
###使用模块
###安装第三方模块
##面向对象编程
###类和示例
###访问限制
###继承和多态
###获取对象信息
###实例属性和类属性
##面向对象高级编程
###使用__slots__
###使用@property
###多重继承
###定制类
###使用枚举类
###使用元类
##错误、调试和测试
###错误处理
###调试
###单元测试
###文档测试
##IO编程
###文件读写
###StringIO和BytesIO
###操作文件和目录
###序列化
##进程和线程
###多进程
###多线程
###ThreadLocal
###进程 vs 线程
###分布式进程
##正则表达式
