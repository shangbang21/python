
#-*-coding=utf-8-*-
'''
题目：
对10个数进行排序。
'''
import random
l1 = []
for x in range(10):
	l1.append(x + random.randint(9,99))
print(l1)
l2 = sorted(l1,reverse = True)
print(l2)
print(l1)
l1.sort(reverse = True)
print(l1)