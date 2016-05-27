# -*- coding:utf-8 -*-
#定义数组
classmates = ['zhang','sun','li']
print("链表=", classmates)
print("链表长度=", len(classmates))
print("访问链表中的第2个元素=", classmates[1])
print('链表追加一个元素')
classmates.append('追加的元素')
print("追加后=",classmates)
print('在第二的位置插入一个2')
classmates.insert(1,'2')
print('插入后=', classmates)
print("删除末尾元素pop")
classmates.pop()
print('删除末尾后=',classmates)
print('删除第二个元素')
classmates.pop(1)
print('删除第二个元素后=',classmates)
print("将第一个元素替成1")
classmates[0]=1
print("替换后=",classmates)
print('数组中的一个元素有是一个数组')
l1=[2.1,2.2,2.3]
l2=[1,l1,3]
print(l2)
print('访问2.2=', l2[1][1])
l=[]
print('空数组',l,len(l))