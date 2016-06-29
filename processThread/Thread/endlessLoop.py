# -*- coding:utf-8 -*-
#
print('一个死循环的例子：')
import threading, multiprocessing
def loop():
	x = 0
	while True:
		print(x)

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()
