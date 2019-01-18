'''
题目：
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
x + 100 = sqrt(x + 100)*sqrt(x + 100)
x + 168 = sqrt(x + 168)*sqrt(x + 168)
'''
import math
def search(x):
	i = 1
	L = []
	while i < x:
		if math.sqrt(i + 100) * math.sqrt(i + 100) == i + 100 and math.sqrt(i + 100) % 1 == 0:
			if math.sqrt(i + 268) * math.sqrt(i + 268) == i + 268 and math.sqrt(i + 268) % 1 == 0:
				L.append(i)
		i += 1
	return L


if __name__ == '__main__':
	x = int(input('需要查找多少以内的数字：'))
	L = search(x)
	n = len(L)
	if n < 1:
		print('输入的范围内没有满足条件的数字！' )
	else:
		print('查找出了%s个该数，结果是：' % len(L), L)