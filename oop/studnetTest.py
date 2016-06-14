# -*- coding:utf-8 -*-
print("定义一个学生类：")
class Student(object):
    def __init__(self,name,score):#第一个参数是self，表示实例本身
        self.name=name
        self.score=score
    
    def print_score(self):
        print('%s:%s' % (self.name, self.score))

print("创建学生实例并输出成绩：")
bart = Student('Bart',59)#不需要传入self
lisa = Student('Lisa', 87)

if __name__=='__main__':
    lisa.print_score()#也不需要传入self
    bart.print_score();
    bart.sex='男'#自由的给实例添加属性，或者通过构造方法
    
#
print('创建私有变量：')
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))
        
tom = Student('Tom', 18)
tom.print_score()
#print(tom.__name) #这里报错，说没有__name属性
tom.__name='123'
tom.print_score()
print(tom.__name) #这里却没有报错，因为上面我们给这个实例一个__name属性

#
print('继承和多态：')
print('定义animal类：')
class Animal(object):
    def run(self):
        print('Animal is running...')
print("定义Dog和Cat类：")
class Dog(Animal):
    pass
class Cat(Animal):
    def run(self):#重写父类的方法
        print('Cat is running...')
    def eat(self):
        print('Cat is eating...')

dog = Dog()
cat = Cat()
dog.run()
cat.run()

print('判断一个变量是否是某种类型：')
print(isinstance(dog,Animal)) #True
print(isinstance(dog, Cat)) #False













