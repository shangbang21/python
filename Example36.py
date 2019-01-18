#-*-coding=utf-8-*-
'''
题目：
求100之内的素数。
'''
l1 = []
for x in range(2,101):
	loop = 0
	for y in range(2,x):
		if x % y == 0:
			loop = 1
			break
	if loop == 0:
		l1.append(x)

print(l1,sum(l1))