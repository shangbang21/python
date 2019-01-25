#-*-coding=utf-8-*-
'''
题目：
创建一个链表。
'''
l1 = list(range(100))
for x in l1:
	if x % 2 != 0:
		l1.pop(l1.index(x))
print(l1,len(l1))
