# -*- coding:utf-8 -*-
print('使用断言来进行调试：')
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10/n

foo('1')

#
print('通过logging来调试：')
import logging
logging.basicConfig(level=logging.INFO) #定义logging的输出级别
s = '1'
n = int(s)
logging.info('n=%d' % n)
print(10/n)

#
print('通过pdg.set_trace()来进行调试：')
import pdb
s = "0"
n = int(s)
pdb.set_trace() # 程序到这里自动暂停
print(n)
print(10/n)
