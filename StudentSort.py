class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        n=self.score.__cmp__(s.score)
        if n==0:
            n=self.name.__cmp__(s.name)
        return n

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)