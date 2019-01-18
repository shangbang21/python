#-*-coding=utf-8-*-
'''
题目：
一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。

'''
L2 = []
for x in range(1,4355):
	if x == 4354:
		print('跑完了')
	y = 1
	L1 = []
	while y < x:
		if x % y == 0:
			L1.append(y)
		y += 1
	if sum(L1) == x:
		print(L1)
		L2.append(x)
print(L2)
