#-*-coding=utf-8-*-
'''
题目：
模仿静态变量(static)另一案例。
'''
class Static(object):
	"""docstring for Static"""
	num = 0
	def func():
		num += 1


if __name__ == '__main__':
	a = Static()
	for x in range(1,10):
		a.num = x
		print(a.num)