# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    try:
        print('    子进程%s(%s)开始执行：' % (name,os.getpid()))
        start = time.time()
        time.sleep(random.random()*3)
        end = time.time()
        print('    子进程%s(%s)执行了%0.4f秒' % (name, os.getpid(), end-start))
    except Exception as e:
        print(e)

if __name__=='__main__':
    print('父进程%s开始执行：' % os.getpid())
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,) )
    print('等待所有进程执行完成')
    p.close()
    p.join()
    print('所有进程执行完成。')