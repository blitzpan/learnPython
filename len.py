class Fib(object):

    def __init__(self, num):
        self.fibs = [0,1]
        i=2
        while i<num:
            self.fibs.append(self.fibs[i-2]+self.fibs[i-1])
            i=i+1

    def __len__(self):
        return len(self.fibs)
    def __str__(self):
        return str(self.fibs)

f = Fib(10)
print f
print len(f)