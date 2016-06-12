# -*- coding:utf-8 -*-
#偏函数partial
print('把字符串转成数字：')
print(int('123456'))
print(int('123456',base=8)) #把8进制的字符串转换成10进制的数字输出
print(int('12E456',16))
#
print('偏函数：')
import functools
int2 = functools.partial(int, base=2) #2进制的字符串转换成10进制输出
print(int2('100000'))

#
print('求最大值：')
max2 = functools.partial(max, 10)
print(max2(2,4,5))