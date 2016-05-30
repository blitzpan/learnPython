# -*- coding:utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x 
    else:
        return -x 
        
print(my_abs(-5))
#print(my_abs('a'))

import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)

#一元二次方程的解法
def quadratic(a,b,c):
    if a==0:
        return -c/b
    else:
        temp = math.sqrt(b*b-4*a*c)
        return (temp-b)/(2*a),(-temp-b)/(2*a)
print(quadratic(2,3,1))
print(quadratic(1,3,-4))

#可变参数，即参数的个数不确定
def calc(numbers):
    sum=0
    for x in numbers:
        sum = sum+x*x 
    return sum 
#参数作为一个list或者tuple传入，可以变相实现可变参数
print("可变参数第一种调用=",calc([1,2,3]))

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

#关键字参数
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

#命名关键字参数
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