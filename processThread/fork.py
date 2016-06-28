# -*- coding:utf-8 -*-
#
print("轻松创建子进程：fork函数会返回两次。")
import os
print('Process (%s) start...' % os.getpid())
# 只在Unix/Linux/Mac上面起作用，windows不能运行
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))