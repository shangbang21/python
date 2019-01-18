#-*-coding=utf-8-*-
'''
题目：
求一个3*3矩阵主对角线元素之和。
'''
import random
#生成一个三维list
l1 = []
for x in range(3):
	l2 = []
	for y in range(3):
		l2.append(random.randint(100,215))
	l1.append(l2)
print(l1)
#拆分计算3维list


l4 = []
for x in range(3):
	l3 = []
	for y in range(3):
		if x == 0:
			l3.append(l1[y][y])		
		elif x == 1:
			l3.append(l1[y][x])
		elif x == 2:
			a = x - y
			l3.append(l1[y][a])
	print('sum=',sum(l3))
	l4.append(l3)
print(l4)








a = [8,3,6,5,34,17,28,9,2]
min,max = a[0],a[0]

for y in a:
	if min > y:
		min = y
	elif max < y:
		max = y
print(min,max)