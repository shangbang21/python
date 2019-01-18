
#-*-coding=utf-8-*-
#!usr/bin/python
'''
题目：
打印出如下图案（菱形）:
'''

def res(x):
	n = 21
	for x in range(1,n//2+2):
		print(' ')
		for y in range(n//2+1-x):
			print(' ',end = '')
		for z in range(x*2-1):
			print('*',end = '')
	for a in range(1,n//2+1):
		print(' ')
		for y in range(a):
			print(' ',end = '')
		for z in range(n-2*a):
			print('*',end = '')
print('')



if __name__ == '__main__':
	x = int(input('请输入菱形的边长：'))
	if x % 2 != 1:
		print('可能输入基数边长的话，这个菱形要漂亮一点！')
	res(x)