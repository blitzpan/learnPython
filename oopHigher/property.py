# -*- coding:utf-8 -*-
class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("必须是数字类型！")
        if value<0 or value>100:
            raise ValueError("必须在0到100之间！")
        self.__score = value

s = Student()
s.score = 100 #对外是直接操作了变量score，实际上我们是调用了一个set方法，那么在这个方法中，我们就可以对set的值进行一系列的校验。
print(s.score)
#s.score = "zhangsan" #会抛出异常

#
print('请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：')
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    @property
    def resolution(self):
        return self.__width * self.__height

s = Screen()
s.width=1024
s.height=768
print(s.resolution)