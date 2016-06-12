# -*- coding:utf-8 -*-

'a test module' #模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__='god pan' #把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import sys
def test():
    args  = sys.argv #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    #命令行测试，打开改文件夹，按住shift，右键点击在此打开命令行窗口，然后执行python moduleTest1.py hehe
    print(args)
    if len(args)==1:
        print('Hello world！')
    elif len(args)==2:
        print('hello,%s' % args[1])
    else:
        print('太多的参数！')

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()

#
print('作用域：')
def _private1(name):
    return 'hello,%s' % name
def __private2(name):
    return 'hi,%s' % name
def greeting(name):
    if len(name)>3:
        return _private1(name)
    else:
        return __private2(name)
print(greeting('xiaoming'))
print(greeting('li'))

#
print('调用第三方模块生成缩略图：')
from PIL import Image
im = Image.open('D:/lifeIsTough/learnPython/module/test.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('D:/lifeIsTough/learnPython/module/thumb.jpg','JPEG')





















