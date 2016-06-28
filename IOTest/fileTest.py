# -*- coding:utf-8 -*-

filePath = 'D:/lifeIsTough/learnPython/IOTest/testFile.txt'
print('读文件：')
try:
    f = open(filePath, 'r')
    content = f.read()
    print(content)
finally: #文件必须关闭，finally防止出现异常，文件没有关闭的情况
    if f:
        f.close()
        
#
print('with语法自动关闭文件。')
with open(filePath, 'r') as f:
    print(f.read())
    
print('readline：')
with open(filePath, 'r') as f:
    oneL = f.readline().strip()
    while oneL != '':
        print(oneL) #把末尾的\n去掉
        oneL = f.readline().strip()

print('write：')
with open(filePath, 'w') as f:
    f.write('hello world')
    
#
print('写入StringIO：')
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue()) #获取写入后的str
#
print('读取StringIO：')
f = StringIO('Hello!\n Hi!\nGoodBye!')
while True:
    s = f.readline()
    if s=='':
        break
    print(s.strip())
#
print('写入BytesIO：')
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) #注意，这里写入的不是str，而是tytes
print(f.getvalue())
#b'\xe4\xb8\xad\xe6\x96\x87'

#
print("读取BytesIO:")
from io import StringIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
content = f.read()
print(content)
print(content.decode('utf-8'))

#
print("操作文件和目录：")
#
print("查看当前目录的绝对路径：")
import os,os.path
print(os.path.abspath('.'))
print("在某个目录下创建一个新目录：")
#创建一个目录
#os.mkdir('d:/testDir') #当已经存在的时候，再次创建会报错
#先把新目录的完整路径表示出来：
newPath = os.path.join('d:/testDir','test1') #用这种方法来获取一个路径，可以正确处理不同的操作系统的路径分隔符。Linux返回/，windows返回\
# 但是注意，盘符后面的是/
print(newPath)
os.mkdir(newPath)
#
print('删除一个目录：')
os.rmdir(newPath)
print('拆分路径，也不要直接拆分，要用os.path.split()，把路径拆分成两部分，后部分是目录或者文件名：')
pathArr = os.path.split(newPath)
print(pathArr)
#这些join合并、split拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

#
filePath = os.path.join('D:/testDir','test.txt')
print("文件重命名：")
# 重命名的路径如果和原路径不一致，那么是移动+重命名，如果不写路径，那么把文件移动到了当前程序所在的路径
# os.rename(filePath,os.path.join('D:/testDir','test1.txt'))

#
print('列出当前目录的所有目录：')
dirs = [x for x in os.listdir('.') if os.path.isdir(x)] #遍历每一个元素，把符合的放入数组中
print(dirs)

#
print("列出所有的xml文件：")
files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.xml'] #获取所有以.xml结尾的文件
print(files)

#
print('实现dir -l')
def dir_l():
    files = os.listdir('.')
    for f in files:
        if os.path.isdir(f):
            print('d', f)
        else:
            print('f', f)
while True:
    command = input("请输入命令：")
    if command=='q':
        print('退出！')
        break
    elif command=='dir -l':
        dir_l()
        break
    else:
        print("命令不存在！")

#
print('编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。')
def findFile(curP, value):
    dirs = os.listdir(curP)
    for d in dirs:
        if os.path.isdir(d):
            findFile(os.path.join(curP,d), value)
        else:
            if value in d:
                print(os.path.join(curP,d))

findFile('.', '.xml')
















