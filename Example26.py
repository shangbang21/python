#-*-coding=utf-8-*-
'''
题目：
利用递归方法求5!。
'''

def jc(x):
	if x == 1:
		return 1
	else:
		return x * jc(x - 1)


if __name__ == '__main__':
	s = 5
	num = jc(s)
	print(num)
