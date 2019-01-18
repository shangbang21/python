#-*-coding=utf-8-*-
'''
题目：
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

a = 8

l1 = [2,4,6,8,10]
y = 0
if l1[0] > l1[1]:
	for x in l1:
		if a > x:
			l1.insert(y,a)
			break
		y += 1
else:
	for x in l1:
		if a > x:
			l1.insert(y,a)
		break
		y += 1

print(l1)