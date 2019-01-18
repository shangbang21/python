#-*-coding=utf-8-*-
'''
题目：
使用lambda来创建匿名函数。
'''

def func(x):
	return lambda x : x ** 2
if __name__ == '__main__':
	a = 5
	b = lambda a:a**2
	print(b(5))
	l1 = []
	for x in range(1,11):
		l1.append(b(x))
	print(l1)
	l2 = []
	# l2 = list(map(lambda a:a**2,range(5,10)))
	l2 = list(map(func(x),range(5,10)))
	print(l2)

	L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
	print(L)