#-*-coding=utf-8-*-
'''
题目：
练习函数调用。

'''
def func(x):
	print('练习函数调用,第%d次' % x)

if __name__ == '__main__':
	for x in range(10):
		x += 1
		func(x)

