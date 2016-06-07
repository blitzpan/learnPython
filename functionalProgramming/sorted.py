# -*- coding:utf-8 -*-
#
print("对list进行排序；")
L = [36,5,-12,9,-21]
l = sorted(L)
print(l)
#
print("按照绝对值大小进行排序：")
l = sorted(L, key=abs)
print(l)
#
print("对字符串排序：")
L = ['bob', 'about', 'Zoo', 'Credit']
l = sorted(L)
print(l)
#
print("字符串忽略大小写进行排序：")
l = sorted(L, key=str.lower)
print(l)
#
print("反向排序：")
l = sorted(L, key=str.lower, reverse=True)
print(l)
#
print("按学生姓名排序：")
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return str.lower(t[0])
L2 = sorted(L, key=by_name)
print(L2)
#
print("按照学生成绩排序：")
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)

