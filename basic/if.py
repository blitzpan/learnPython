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
    
    