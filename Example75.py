#-*-coding=utf-8-*-
'''
题目：
放松一下，算一道简单的题目。
'''
l1 = list(range(5))
sum = 0
def func(x):
	return x**2
for x in l1:
	sum += func(x)
print(sum)

 #    *
 #   ***
 #  *****
 # *******
 #  *****
 #   ***
 #    *
s = sum
for x in range(s):
	for i in range(s - x):
		print(' ',end = '')
	for j in range(x * 2 + 1):
		print('*',end = '')
	print()
for x in range(s - 1):
	for i in range(x + 2):
		print(' ',end = '')
	for j in range(s*2 - 2*x -3):
		print('*',end = '')
	print()