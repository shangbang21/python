#-*-coding=utf-8-*-
'''
题目：
有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''
l2 = [1,2,3,4,5,6,7,8]
l3 = []
a = 3
for x in range(a):
	i = len(l2) - a + x
	l3.append(l2[i])
	l2.pop(i)

print(l2)
print(l3)
l3 += l2
print(l3)