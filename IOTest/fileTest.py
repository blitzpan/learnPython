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
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#b'\xe4\xb8\xad\xe6\x96\x87'














