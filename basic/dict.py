# -*- coding:utf-8 -*-
#初始化
d={}
d={"li":"liSi",'wang':'wangWu'}
#新增
d['zhang']='zhangSan'
print(d['zhang'])
print(d['wang'])
#取值的时候，如果key不存在，那么会报错，解决办法是：
#1. in操作
ifIn = 'zhang' in d
print(ifIn)
#2. get操作：不存在返回None或者如果有默认值返回默认值
print(d.get('zhang'))
print(d.get('zhang1'))
print(d.get('zhang1','zhang1不存在。'))


#set使用list操作构造参数
s=set([1,2,3])
print(s)
#set新增
s.add(4)
print(s)
#set删除
s.remove(4)
print(s)
#set求交集、并集
s2=set([3,4,5,6])
print("交集=", s & s2)
print("并集=", s | s2)
