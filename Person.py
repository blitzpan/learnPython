class Person(object):
    def __init__(self,name,gender,birth):
        self.name=name
        self.gender=gender
        self.birth=birth

xiaoming=Person('xiaoming','M','1991')
xiaohong=Person('xiaohong','F','1992')
print xiaoming,xiaoming.name,xiaohong.birth