#-*-coding=utf-8-*-
'''
题目：
判断101-200之间有多少个素数，并输出所有素数。
'''
import math
L = []

for x in range(101,201):
	b = 1
	for y in range(2,int(math.sqrt(x)+1)):
		if x % y == 0:
			b = 0
			break
	if b == 1:
		L.append(x)

print('范围内共有%s个素数！他们是：'% len(L),L)
