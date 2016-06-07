# -*- coding:utf-8 -*-
def triangles(num):
	L=[1]
	while len(L)<num:
		print(L)
		#yield L
		L = [L[n-1] + L[n] for n in range(len(L))]
		print('=============',L)
		L.append(1)
		L[0] = 1
triangles(6)