# -*- coding:utf-8 -*-
import time, threading

#银行存款（给线程加锁）
balance = 0
lock = threading.Lock()
def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n 
    
def run_thread(n):
    for i in range(100000): #共执行100000先存后取
        #先获得锁
        lock.acquire()
        try:
            change_it(n) #放心的改，这回不会因为多线程引起异常数据了
        finally:
            #改完了一定要释放锁
            lock.release()
    print('线程执行完成。')

t1 = threading.Thread(target=run_thread, args=(500,))
t2 = threading.Thread(target=run_thread, args=(800000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)