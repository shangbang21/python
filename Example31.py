#-*-coding=utf-8-*-
'''
题目：
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
l1 = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
l2 = [1,2,3,4,5,6,7]
l3 = []

a = input('第一个字母')
for x in l1:
	if x[0] == a:
		l3.append(x)
if len(l3) == 1:
	b = len(l3)
	print(l1[l1.index(l3[0])])
else:
	i = input('第二个字母')
	for j in l3:
		if j[1] == i:
			print(j)