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
#
print('求出全体素数。')
#先构造一个从3开始的奇数序列：
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#定义一个筛选条件：
def _not_divisible(n):
    return lambda x:x%n>0#不能被整除返回true
def primes():
    yield 2
    it = _odd_iter()#初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
for n in primes():
    if n<1000: #由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
        print(n)
    else:
        break 

#
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

    
print('123456789'[::-2])










