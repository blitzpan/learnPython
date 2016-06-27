# -*- coding:utf-8 -*-
try:
    print('try...')
    r = 10/0
    print('result=', r)
except ValueError as e:
    print('ValueError:' , e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('如果添加了else，并且程序没有错误的话，执行else语句。')
finally:
    print('finally...')
print('END')

#
print('打印日志：')
import logging
try:
    print(10/0)
except Exception as e:
    logging.exception(e)
finally:
    print('End')

#
print("抛出异常：")
class FooError(ValueError):
    pass
    
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value:%s' % s)
    return 10/n
foo('0')
    
    