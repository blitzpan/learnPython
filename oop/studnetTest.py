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

print('获取对象信息：')
print('使用type()判断对象类型：')
print(type(123))
print(type('123'))
print("是否是字符串类型：", type('123')==str)
print(type(None))
print('使用type()来判断函数：')
print(type(abs))
print('判断一个对象是否是函数，用types模块中定义的常量：')
import types
def fun():    pass
print( type(fun)==types.FunctionType ) #True
print( type(abs)==types.BuiltinFunctionType ) #True
print( type(lambda x:x)==types.LambdaType ) #True
print( type(x for x in range(10))==types.GeneratorType ) #True

#
print('使用isinstance()：')
print(isinstance('abc', str))
print('判断一个变量是否在某些类型中：')
print( isinstance([1,2,3], (list,tuple)) )

#
print("使用dir()：")
print( dir('abc') )

#
class MyObj(object):    def __len__(self):
        return 100
    def print(self):
        print('myObj print...')

print("自定义对象的长度=", len(MyObj()) )

#getattr/setattr/hasattr
mo = MyObj()
if hasattr(mo, 'x'):#有属性'x'吗
    print('有属性x')
    print(mo.x)
else:
    print('没有属性x')
    setattr(mo, 'x', 10) #设置属性x
if hasattr(mo, 'x'):#有属性'x'吗
    print('有属性x')
    print(mo.x)
    print( getattr(mo, 'x') )

print('获取一个不存在的属性，会抛出异常：')
#getattr(mo, 'y')
print( getattr(mo, 'y', 404) )  #设置默认值，如果该属性不存在，那么返回一个默认值

#
print('获取一个对象的方法：')
fn = getattr(mo, 'print')
fn() #相当于调用了mo.print()

#
print("实例属性、类属性：")
class Student(object):
    country='中国' #类属性
    def __init__(self,name):
        self.name=name #实例属性
li = Student('Li')
print(li.country, li.name)
print('打印类属性和实例属性：')
print(Student.country, li.country)
li.country = '我是中国人' #给实例一个country属性
print(Student.country, li.country)#会发现同名的实例属性和类属性同时存在
del li.country #删除实例属性
print(Student.country, li.country) #类属性仍然存在

















