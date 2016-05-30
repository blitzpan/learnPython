# -*- coding:utf-8 -*-
names=['zhang','li','wang']
for name in names:
    print(name)
#求1到10的和：
print("求1到10的和：")
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print("1加到10=", sum)
#range
print(list(range(10)))
#求0到100的和：
print('求0到100的和：')
sum=0
for x in range(101):
    sum = sum + x 
print(sum)
#求100以内所有奇数的和
sum=0
n=1 
while n<100:
    sum = sum+n
    n=n+2
print(sum)