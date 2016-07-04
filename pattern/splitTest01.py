# -*- coding:utf-8 -*-
import re
oldStr = 'a b     c'
resList = oldStr.split(' ')
print("正常的切分无法识别连续的空格：")
print(resList)
print('正则切分：')
resList = re.split(r'\s+', oldStr)
print(resList)
print('对空格和逗号进行分割：')
resList = re.split(r'[\s\,]+', 'a,b, c d')
print(resList)
print('对空格、逗号和分号进行分割：')
resList = re.split(r'[\s\,\;]+', 'a,b;; c d')
print(resList)
