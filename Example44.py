#-*-coding=utf-8-*-
'''
题目：
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
'''
import random
l1 = []
l2 = []

for x in range(3):
	l3 = []
	l4 = []
	for y in range(3):
		l3.append(random.randint(15,25))
		l4.append(random.randint(35,45))
	l1.append(l3)
	l2.append(l4)

print(l1,'\n',l2)

l5 = []
for i in range(len(l1)):
	l6 = []
	sum = 0
	for j in range(len(l2)):
		sum = l1[i][j] +l2[i][j]
		l6.append(sum)
	l5.append(l6)
print(l5)


