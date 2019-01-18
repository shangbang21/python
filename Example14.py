#-*-coding=utf-8-*-
'''
题目：
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
import math
num = 90
L = []
for x in range(2,int(math.sqrt(num))):
	while num % x == 0:
		num = num / x
		L.append(x)

print(L)