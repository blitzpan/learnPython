# -*- coding:utf-8 -*-
# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

print('以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：')

#写数据进程执行的代码
def write(q):
    print("写进程：%s" % os.getpid())
    for value in ['A','B','C','D']:
        print('把%s放入队列。' % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    print('读进程：%s' % os.getpid())
    while True:
        value = q.get(True)
        print('从队列中获取：%s' % value)
        
if __name__=='__main__':
    #父进程创建Queue，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程是死循环，无法等待其结束，只能强行终止：
    pr.terminate()