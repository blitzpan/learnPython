# -*- coding:utf-8 -*-
import threading
#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
	#获取当前线程关联的student
	std = local_school.student
	print('线程%s中的name=%s' % (threading.current_thread().name, std))
def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student=name
	process_student()
t1 = threading.Thread(target=process_thread, args=('Alice',))
t2= threading.Thread(target=process_thread, args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()
