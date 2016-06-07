# -*- coding:utf-8 -*-
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
print('利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。')
def normalize(name):
    name = name[:1].upper()+name[1:].lower()
    return name 
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：')
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y ,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print("利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：")
CHAR_TO_FLOAT={
 '0':0,
 '1':1,
 '2':2,
 '3':3,
 '4':4,
 '5':5,
 '6':6,
 '7':7,
 '8':8,
 '9':9,
 '.':-1
}
def str2float(s):
    nums = map(lambda x:CHAR_TO_FLOAT[x], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n==-1:
            point=1
            return f
        if point==0:
            return f*10+n
        else:
            point = point * 10
            return f + n/point
    return reduce(to_float, nums, 0)
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







