# -*- coding:utf-8 -*-
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    for x in range(10):
        print('    子进程%s(%s)' % (name, os.getpid() ))
        
if __name__=='__main__':
    print('父进程%s' % os.getpid())
    sonP = Process(target=run_proc, args=('son1',))
    sonP.start()
    sonP.join() #join使该进程执行完之后程序再往下执行
    print('子进程执行完成。')