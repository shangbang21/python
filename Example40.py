#-*-coding=utf-8-*-
'''
题目：
将一个数组逆序输出。
'''
l1 = list(range(3,150,9))
print(l1)
l2 = l1[::-1]
print(l2)
x = len(l2) - 1
while x >= 0:
	print(l2[x])
	x -= 1
