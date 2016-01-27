# -*- coding:utf-8 -*-
#求两个数的最小公约数
def gcb(m,n):
    if n==0:
        return m
    else:
        return gcb(n, m%n)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p*r.q-self.q*r.p,self.q*r.q)

    def __mul__(self, r):
        return Rational(self.p*r.p,self.q*r.q)

    def __div__(self, r):
        return Rational(self.p*r.q,self.q*r.p)

    def __str__(self):
        ys = gcb(self.p, self.q)
        return '%s/%s'%(self.p/ys,self.q/ys)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2