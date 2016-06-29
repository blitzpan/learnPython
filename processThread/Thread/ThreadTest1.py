# -*- coding:utf-8 -*-
import time, threading
# 新线程执行的代码
def loop():
	print('线程%s运行中' % threading.current_thread().name)
	n = 0
	while n<5:
		n = n+1
		print("线程%s>>>%s" % (threading.current_thread().name, n))
		time.sleep(1)
	print("线程%s停止！" % threading.current_thread().name)	

print('线程%s正在运行中。。。' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('线程%s停止！' % threading.current_thread().name)
