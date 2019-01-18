#-*-coding=utf-8-*-
'''
题目：
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

def func(x):
	y = str(x)
	num = 0
	l = []
	for a in y:
		num += 1
		l.append(a)
	l.reverse()
	return num,l

if __name__ == '__main__':
	a = 876
	b = func(a)
	print('共%s位数。倒序结果：%s'%(b[0],b[1]))
	print(type(b),type(b[0]),type(b[1]))
