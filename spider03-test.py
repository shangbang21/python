#!usr/bin/python
# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests, sys
import pdb

class downloader(object):
	"""docstring for downloader"""
	def __init__(self):
		self.server = 'http://www.biqukan.com'
		self.target = 'http://www.biqukan.com/1_1094/'
		self.names = []		#存放章节名
		self.urls = []		#存放章节链接
		self.nums = 0		#章节数
	#获取章节链接
	def get_download_url(self):
		req_obj = requests.get(self.target)
		bsf_obj = BeautifulSoup(req_obj.text,  features = "html.parser")
		div_obj = bsf_obj.find_all('div', class_ = 'listmain')
		a_obj = BeautifulSoup(str(div_obj), features = 'html.parser')
		a_list = a_obj.find_all('a')
		self.nums = len(a_list[16:])
		print(self.nums)
		for x in a_list[16:]:
			self.names.append(x.string)
			self.urls.append(self.server + x.get('href'))

	#获取章节内容
	def get_contents(self, target):
		req_obj = requests.get(target)
		bsf_obj = BeautifulSoup(req_obj.text,  features = "html.parser")
		# print(bsf_obj)
		div_obj = bsf_obj.find_all('div', class_ = 'showtxt')
		while len(div_obj) == 0:
			# print('出错了！',div_obj, target, req_obj.text)
			# print('出错了！',div_obj, target)
			req_obj = requests.get(target)
			bsf_obj = BeautifulSoup(req_obj.text,  features = "html.parser")
			div_obj = bsf_obj.find_all('div', class_ = 'showtxt')
		# pdb.set_trace()
		txt_obj = div_obj[0].text.replace('\xa0' * 8, '\n')
		return txt_obj

	def writer(self, name, path, text):
		write_flag = True
		with open(path, 'a', encoding = 'utf-8') as f:
			f.write(name + '\n')
			f.writelines(text)
			f.write('\n\n')


if __name__ == '__main__':
	doc = downloader()
	doc.get_download_url()
	print('<一念永恒>开始下载：')
	for x in range(doc.nums):
		y = x + 1
		print('第%d章，%s    开始下载！ 下载地址：%s ' % (y, doc.names[x], doc.urls[x]))
		texts = doc.get_contents(doc.urls[x])
		# print(texts)
		# doc.writer(doc.names[x], '一念永恒.txt', doc.get_contents(doc.urls[x]))
		doc.writer(doc.names[x], '一念永恒.txt', texts)
		sys.stdout.write('已下载：%.3f%%' % float(x/doc.nums) + '\r')
		sys.stdout.flush()
	print('<一念永恒>下载OK!')