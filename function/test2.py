# -*- coding:utf-8 -*-
def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n
print(fact(100))
# 汉诺塔
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)#只有一个直接移动
    else:
        move(n-1,a,c,b)#将n-1个从a移动到b上
        print(a,'-->',c)#将第n个从a移到c上
        move(n-1,b,a,c)#将n-1个从b移到c上
move(3,'A','B','C')