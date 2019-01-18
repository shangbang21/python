#-*-coding=utf-8-*-
'''
题目：
按相反的顺序输出列表的值。
'''
l = [8,1,6,5,4,3]
l1 = [8,1,6,5,4,3]
l2 = []
#方法1
for x in range(len(l1)):
	l2.append(l1[len(l1) - x - 1])
print(l2)
#方法2
l3 = l1[::-1]
print(l3)
#方法3
l1.reverse()
print(l1)
#方法4
l4 = list(reversed(l))
print(l4)
