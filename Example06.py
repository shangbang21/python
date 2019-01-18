#-*-coding=utf-8-*-
'''
题目：
斐波那契数列。
'''
# a,b = 0,1
# num = 100
# x = 0
# while x < num:
# 	print(a)
# 	a,b = b,a+b
# 	x += 1
a,b = 0,1
for x in range(100):
	print(a)
	a,b = b, a+b
