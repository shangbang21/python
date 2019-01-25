#-*-coding=utf-8-*-
'''
9
9 * 10 + 9 
99 *10 + 9
题目：
输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
'''
a = 13
x = 9
y = 0
while True:
	y += 1
	if x % a == 0:
		print(x, y)
		break
	else:
		x = x*10 + 9