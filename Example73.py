#-*-coding=utf-8-*-
'''
题目：
反向输出一个链表。
'''

l1 = list(range(3,100,4))
print(l1)
l2 = l1[::-1]
print(l2)
l3 = list(reversed(l1))
print(l3)
l1.reverse()
print(l1)
l1.reverse()
print(l1)

i = len(l1)
l4 = []
for x in l1:
	l4.append(l1[i - 1])
	i -= 1
print(l4)