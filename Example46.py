#-*-coding=utf-8-*-
'''
题目：
求输入数字的平方，如果平方运算后小于 50 则退出。
'''
a = 5

def func(x):
	return x**2

if __name__ == '__main__':
	a = int(input('请输入一个数字：'))
	b = func(a)
	if b < 50:
		pass
	else:
		print(b)
	c = 1
	while c:
		a = int(input('请输入一个数字：'))
		b = func(a)
		if b < 50:
			c = 0
		else:
			print(b)