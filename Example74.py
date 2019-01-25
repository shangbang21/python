#-*-coding=utf-8-*-
'''
题目：
列表排序及连接。
'''
import random
l1 = []
l2 = []

for x in range(10):
	if x % 2 != 0:
		l1.append(x + random.randint(1,15))
	else:
		l2.append(x + random.randint(1,15))
l3 = l1 + l2
print(l1,'\n',l2,'\n',l3)
# l1.sort()
# l2.sort()
l3.sort()
print(l1,'\n',l2,'\n',l3)
l4 = sorted(l1)
l5 = sorted(l2)
print(l4,'\n',l5)