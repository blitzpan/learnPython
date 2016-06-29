# -*- coding:utf-8 -*-
import time, threading

#银行存款（一个错误的例子，最后的结果不一定为0）
balance = 0
def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n 
    #print(balance)
    
def run_thread(n):
    for i in range(100000): #共执行100000先存后取
        change_it(n)
    print('线程执行完成。')

t1 = threading.Thread(target=run_thread, args=(500,))
t2 = threading.Thread(target=run_thread, args=(800000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


