# -*- coding:utf-8 -*-
#ƫ����
import functools
int2 = functools.partial(int, base=2)
print int2('10000'),int('10000',2)
print int2('101001'),int('101001',2)