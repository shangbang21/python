#-*-coding=utf-8-*-
'''
题目：
两个变量值互换。
'''
def swap(x, y):
	x, y = y, x
	return x, y

if __name__ == '__main__':
	a = 10
	b = 15
	print(a,b)
	a,b = swap(a,b)
	print(a,b)