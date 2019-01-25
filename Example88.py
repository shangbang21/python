#-*-coding=utf-8-*-
'''
题目：
读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''
import random
for x in range(7):
	a = random.randint(1,50)
	print(a)
	for y in range(a):
		print('*',end = '')
	print(end = '\n')
print(end = '\n')