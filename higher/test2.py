# -*- coding:utf-8 -*-
from collections import Iterable
#Iterable
print(isinstance([],Iterable))
print(isinstance('abc',Iterable))
#Iterator
from collections import Iterator
print('Iterator')
print(isinstance((x for x in range(10)),Iterator))
#True
print(isinstance([],Iterator))
#False
print("把Iterable变成Iterator可以使用iter()")
print(isinstance(iter([]), Iterator))
#True
