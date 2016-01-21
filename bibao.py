# -*- coding:utf-8 -*-
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            return j*j
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()