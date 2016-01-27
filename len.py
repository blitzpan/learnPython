class Fib(object):

    def __init__(self, num):
        self.fibA = [0,1]
        i=2
         
        while(i<num):
           self.fibA.append(self.fibA[i-2]+self.fibA[i-1])
           i=i+1
           
    def __len__(self):
        return len(self.fibA)

f = Fib(10)
print f
print len(f)