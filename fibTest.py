class Fib(object):
    def __call__(self,num):
        fibs=[0,1]
        i=2
        while i<num:
            fibs.append(fibs[i-2]+fibs[i-1])
            i=i+1
        return fibs
f = Fib()
print f(10)