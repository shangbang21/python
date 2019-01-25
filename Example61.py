#-*-coding=utf-8-*-
'''
题目：
打印出杨辉三角形（要求打印出10行）。　
'''

n = 1
l1 = []

for x in range(15):
	l2 = []
	for y in range(x+1):
		a = 1
		if y == x or y == 0:
			l2.append(a)
		else :
			a = l1[x - 1][y] + l1[x - 1][y - 1]
			l2.append(a)
	l1.append(l2)
	print(l2)
print(l1)