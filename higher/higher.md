###高级特性
####迭代器
>可以直接作用于for循环的数据类型有以下几种：
> * 一类是集合数据类型，list/tuple/dict/set/str
> * 一类是`generator`，包括`生成器`和带`yield`的generator function。
可以直接作用于for循环的对象统称为`可迭代对象`：`Iterable`。

`isinstance`判断一个对象是否是Iterable对象。
```
# -*- coding:utf-8 -*-
#Iterable 
from collections import Iterable
print(isinstance([],Iterable))
#True
print(isinstance('abc',Iterable))
#True
```
而生成器不但可以作用于`for`循环，还可以被`next()`函数不断调用并返回下一个值，知道最后抛出`StopIteration`错误表示无法继续返回下一个值了。可以被`next()`函数调用并不断返回下一个值的对象成为`迭代器`：`Iterator`。

生成器都是`Iterator`对象，但`list、dict、str`虽然是`Iterable`，却不是`Iterator`。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：
```
print("把Iterable变成Iterator可以使用iter()")
print(isinstance(iter([]), Iterator))
#True
```





















