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
###定义函数
###函数的参数
###递归函数

##高级特性
###切片
###迭代
###列表生成式
###生成器
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
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###