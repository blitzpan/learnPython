# -*- coding:utf-8 -*-
from enum import Enum

print("定义一个月份的枚举：")
Month = Enum('MonthTest', ('Jan','Feb','Mar','Apr','May','Jun','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'==>',member,',',member.value)

print(Month.Feb, Month.Feb.value)
#MonthTest.Feb 2
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
