# -*- coding:utf-8 -*-

def fn(self, name='world'): # �ȶ��庯��
    print('Hello, %s' % name)
    
Hello = type('Hello', (object,), dict(hello=fn)) # ����Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))