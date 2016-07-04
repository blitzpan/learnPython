# -*- coding:utf-8 -*-
import re
pattern01 = r'^(\d{3})-(\d{3,8})$'
m = re.match(pattern01, '010-12345')
print(m.group(0)) # 0是指全部字符串
print(m.group(1))
print(m.group(2))
#
print("贪婪匹配：")
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#
print("预编译的正则：")
#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
resList = re_telephone.match("010-12345").groups()
print(resList)
