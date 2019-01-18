#-*-coding=utf-8-*-
'''
题目：
模仿静态变量的用法。
'''
def varfunc():
	var = 0
	print('var = %d' % var)
	var += 1

if __name__ == '__main__':
	for x in range(5):
		varfunc()