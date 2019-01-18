#-*-coding=utf-8-*-
#!usr/bin/python
'''
题目：
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''
a ,b ,c= 2, 1, 0
for x in range(20):
	c += a / b
	print(a, '/' ,b,'=' ,a / b)
	a, b = a + b, a
print(c)
