# -*- coding:utf-8 -*-
from urllib import request
from html.parser import HTMLParser
class MyHtmlParser(HTMLParser):
	def __init__(self):
		super().__init__() #若是不init父类的话会报错。
		self._tag=''
		self._res = {}
		self._count = 0

	def handle_starttag(self, tag, attrs):
		if tag=='h3' and len(attrs)>0 and len(attrs[0])>1 and attrs[0][0]=='class' and attrs[0][1]=='event-title':
			self._tag = 'title'
		if tag=='time' and len(attrs)>0 and len(attrs[0])>1 and attrs[0][0]=='datetime':
			self._tag = 'time'
		if tag=='span' and len(attrs)>0 and len(attrs[0])>1 and attrs[0][0]=='class' and attrs[0][1]=='event-location':
			self._tag = 'addr'
	def handle_data(self, data):
		if self._tag == 'addr':
			self._res[self._count]['addr'] = data
			self._count += 1
		elif self._tag == 'time':
			self._res[self._count]['time'] = data
		elif self._tag == 'title':
			self._res[self._count] = {'title':data}
		self._tag = ''
	def printRes(self):
		for k in self._res:
			print('%s    %s    %s' % (self._res[k]['title'], self._res[k]['time'], self._res[k]['addr']))



if __name__=='__main__':
	data=''
	with request.urlopen('https://www.python.org/events/python-events/') as f:
		data = f.read()
		print('Status:', f.status, f.reason)
	myParse = MyHtmlParser()
	myParse.feed(data.decode('utf-8'))
	myParse.printRes()
